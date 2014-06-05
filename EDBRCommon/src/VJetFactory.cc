#include "ExoDiBosonResonances/EDBRCommon/interface/VJetFactory.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "TLorentzVector.h"
#include "TRandom3.h"

#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetResolution.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include <iostream>

using namespace std;

cmg::VJetFactory::VJetFactory(const edm::ParameterSet& ps):
  jetLabel_(ps.getParameter<edm::InputTag>("inputCollection")),
  prunedJetLabel_(ps.getParameter<edm::InputTag>("prunedJetCollection")),
// add subjet lable here for WH
  subJetLabel_(ps.getParameter<edm::InputTag>("subJetCollection")),

  baseJetFactory_(ps.getParameter<edm::ParameterSet>("baseJetFactory")),
  pfJetFactory_(ps.getParameter<edm::ParameterSet>("pfJetFactory")),
  puVariablesTag_(ps.getParameter<edm::InputTag>("puVariables")), 
  puMvasTag_(ps.getParameter<std::vector<edm::InputTag> >("puMvas")), 
  puIdsTag_(ps.getParameter<std::vector<edm::InputTag> >("puIds")), 
  useConstituents_(ps.getParameter<bool>("useConstituents")) ,
  verbose_(ps.getUntrackedParameter<bool>("verbose")),
  applyResolution_(ps.getParameter<bool>("applyResolution")),
  applyScale_(ps.getParameter<bool>("applyScale")),
  applyScaleDB_(ps.getParameter<bool>("applyScaleFromDB")),
  scaleFile_(ps.getParameter<edm::FileInPath>("scaleFile").fullPath()),
  nSigmaScale_(ps.getParameter<double>("nSigmaScale"))
{
  
  
  if(applyScale_ && verbose_) std::cout<<"For the VJet you are applying the JES with sigma equal to: "<< nSigmaScale_ << std::endl;
  if(applyResolution_ && verbose_) std::cout<<"For the VJet you are applying the JER smearing"<< std::endl;
  if(verbose_)cout<<"VJetFactory::useConstituents is "<<(useConstituents_ ? "True" : "False")<<endl;
  
  // PU discrimination
  // Make sure that MVAs and IDs are in synch and match expectations
  assert( puMvasTag_.size() <= cmg::PFJet::PuIdArray::static_size && 
	  puMvasTag_.size() == puIdsTag_.size() );
  for(size_t ii=0; ii<puIdsTag_.size(); ++ii){
    std::string mvaLabel = puMvasTag_[ii].instance();
    std::string idLabel = puIdsTag_[ii].instance();
    mvaLabel = mvaLabel.substr(0, mvaLabel.find("Discriminant")); 
    idLabel  = idLabel.substr(0, idLabel.find("Id")); 
    assert( mvaLabel == idLabel );
    puNamesTag_.push_back(mvaLabel);
  }
  
}

cmg::VJetFactory::event_ptr cmg::VJetFactory::create(const edm::Event& iEvent, 
						     const edm::EventSetup& iSetup){
  
  //  std::cout<<"\nNew Event:"<<endl;
  edm::Handle<pat::JetCollection> jetCands;
  
  // edm::Handle<reco::PFJetCollection> subJetCands;
  
  cmg::VJetFactory::event_ptr result(new cmg::VJetFactory::collection);
  iEvent.getByLabel(jetLabel_,jetCands);
  
  long unsigned index = 0;
  for(pat::JetCollection::const_iterator mi = jetCands->begin();
      mi != jetCands->end(); ++mi, ++index ){
    
    // Fill PAT jet information of mother jets
    pat::JetPtr jetPtr( jetCands, index ); 
    cmg::VJet structuredcmgjet( jetPtr );
    
    set(iEvent,iSetup,jetPtr,&structuredcmgjet);
    
    result->push_back(structuredcmgjet);
    
  }//end loop on main jet input coll
  
  return result;
}


void cmg::VJetFactory::set(const edm::Event& iEvent, const edm::EventSetup& iSetup,
			   const pat::JetPtr& input, cmg::VJet *output){
  
  
  baseJetFactory_.set(input,&(*output));
  

  //start JES/JER systematic unc
  JetCorrectionUncertainty *jecUnc=0;  
  double unc = 0.0;
  float jesCorrFactor = 0.0;
  float jesSmearFactor = 1.0;
  if(applyScale_){
    if(jecUnc==0){//this is the 1st jet
      if(!applyScaleDB_){//this is deprecated !
	jecUnc=new JetCorrectionUncertainty(scaleFile_.c_str());
      }
      else{
	edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
	iSetup.get<JetCorrectionsRecord>().get("AK7PFchs",JetCorParColl); 
	JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
	jecUnc = new JetCorrectionUncertainty(JetCorPar);
      }
    }//end if 1st jet

    double jetPt = output->pt();
    double jetEta = output->eta();
    double jetMass = output-> mass();
    jecUnc->setJetEta(jetEta);
    jecUnc->setJetPt(jetPt);
    unc = jecUnc->getUncertainty(true);
    jesCorrFactor = unc*nSigmaScale_ ;
    jetPt   = (1+jesCorrFactor)*jetPt;
    jetMass = (1+jesCorrFactor)*jetMass;
    const math::PtEtaPhiMLorentzVector jetp4 (jetPt, output->eta(), output->phi(), jetMass);
    output->setP4(jetp4);  
  }//end if applyScale 

  if(applyResolution_){
    jesSmearFactor = JetResolution(iEvent, output);  
    double jetPt = output->pt();
    double jetMass = output-> mass();
    jetPt   = jesSmearFactor*jetPt;
    jetMass = jesSmearFactor*jetMass;
    const math::PtEtaPhiMLorentzVector jetp4 (jetPt, output->eta(), output->phi(), jetMass);
    output->setP4(jetp4);  
  }//end if applyResolution
  //end JES/JER systematic unc
   
  ///Fill PF Jet specific
  
  // Read PU identification inputs
  edm::Handle<edm::ValueMap<StoredPileupJetIdentifier> > puVariablesTMP;
  iEvent.getByLabel(puVariablesTag_,puVariablesTMP);
  vector<edm::Handle<edm::ValueMap<int> > > puIdsTMP(puIdsTag_.size());
  vector<edm::Handle<edm::ValueMap<float> > > puMvasTMP(puMvasTag_.size());
  for(size_t ii=0; ii<puIdsTag_.size(); ++ii ) {
    iEvent.getByLabel(puIdsTag_[ii],puIdsTMP[ii]);
    iEvent.getByLabel(puMvasTag_[ii],puMvasTMP[ii]);
  }
  
  output->rms_  = (*puVariablesTMP)[input].dR2Mean();
  output->beta_ = (*puVariablesTMP)[input].beta();
  for(size_t ii=0; ii<puIdsTag_.size(); ++ii ) {
    // output->puIdNames_[ii] = puNamesTag_[ii];
    output->puIds_[ii]  = (*puIdsTMP[ii])[input];
    output->puMvas_[ii] = (*puMvasTMP[ii])[input];
  } 
  
  //  std::cout<<"Setting PFJet properties in VJetFactory"<<std::endl;
  pfJetFactory_.setPFproperties(*input,output,useConstituents_);
  
  //Fill VJet specific
  output->qjet_=input->userFloat("qjetsvolatility");
  output->tau1_=input->userFloat("tau1");
  output->tau2_=input->userFloat("tau2");
  output->tau3_=input->userFloat("tau3");
// add tau4/tau5 etc
  output->tau4_=input->userFloat("tau4");
  output->tau5_=input->userFloat("tau5");
 
  // output->mdrop_=
  
  if( prunedJetLabel_.encode().size()){//check that the Input Tag is not empty
    
    edm::Handle<pat::JetCollection> prunedJetCands;
    //loop over pruned jet collection and find the one matching
    //the not-pruned one. From the matched pruned one extract substructure info
    iEvent.getByLabel(prunedJetLabel_,prunedJetCands);
    long unsigned indexTmp=0;
    int index2 = -1;
    double dRmin=99.0;
    for(pat::JetCollection::const_iterator pj = prunedJetCands->begin();
	pj != prunedJetCands->end(); ++pj, ++indexTmp ){
      
      pat::JetPtr pjTMPPtr( prunedJetCands, indexTmp ); 
      double dRtmp=deltaR(*output,*pjTMPPtr);
      if(dRtmp<dRmin && dRtmp<0.7 ){//matching failed if greater than jet radius
	dRmin=dRtmp;
	index2=indexTmp;
      }
    }//end loop on pruned jet collection
    
    if(index2>=0){
      
      pat::JetPtr pjPtr( prunedJetCands, index2 ); 
      output->setPrunedJetPtr(pjPtr);
      
      output->prunedMass_=(float)pjPtr->mass();//pjPtr->correctedJet("Uncorrected").mass()
      
      //JES/JER systematics applied to pruned mass
      if(applyResolution_)output->prunedMass_=(float)pjPtr->mass()*jesSmearFactor;
      if(applyScale_)output->prunedMass_=(float)pjPtr->mass()*(1+jesCorrFactor);

      // if(output->pt()>20.0&&verbose_)cout<<"From VJetFactory: Jet STD/Pruned matched with dR="<<dRmin <<"  -> Mass NOT-Pruned="<<output->mass()<< "  Pruned="<<pjPtr->mass()<<" Pruned-uncorr="<<pjPtr->correctedJet("Uncorrected").mass()<<endl;

      double dau1pt=0., dau2pt=0.; // dau1phi=0., dau2phi=0., dau1eta=0., dau2eta=0.;     
      float nfatjetL=0., nfatjetM=0., nfatjetT=0.; 
      if(pjPtr->daughter(0)!=0  && pjPtr->daughter(1)!=0 && 
	 (pjPtr->daughter(0)->pt()>0.01) &&  (pjPtr->daughter(1)->pt()>0.01)  ) {
	output->mdrop_=float(max(pjPtr->daughter(0)->mass(),pjPtr->daughter(1)->mass())/pjPtr->correctedJet("Uncorrected").mass());
// 
	dau1pt=pjPtr->daughter(0)->pt();
	dau2pt=pjPtr->daughter(1)->pt();

// add fat b jet here for WH
        double fatjet_discCVS = pjPtr->bDiscriminator("combinedSecondaryVertexBJetTags");
	if(fatjet_discCVS>0.244)nfatjetL++;
        if(fatjet_discCVS>0.679)nfatjetM++;
        if(fatjet_discCVS>0.898)nfatjetT++;	
	
        output->nfatjetL_=nfatjetL;
        output->nfatjetM_=nfatjetM;
        output->nfatjetT_=nfatjetT;
      }
      else output->mdrop_=-99.0;

// add sub b jet here for WH
      int flag=0;
      int dex1=-1, dex2=-1;
//      int subjet_flavor=0;
      float subjet1_phi=10., subjet1_eta=10.,subjet2_phi=10.,subjet2_eta=10.;
      float dR_subjet=10.;
      float nsubjetL=0., nsubjetM=0., nsubjetT=0.;
      edm::Handle<pat::JetCollection> subJetCands;
      iEvent.getByLabel(subJetLabel_, subJetCands);
//      for(pat::JetCollection::const_iterator subjet=subJetCands->begin();subjet!=subJetCands->end();++subjet){
      for(unsigned i=0; i<subJetCands->size(); ++i){
//	if(subjet->pt()==dau1pt || subjet->pt()==dau2pt){
//        if((subjet->pt()-dau1pt)<0.01 || (subjet->pt()-dau2pt)<0.01){
//	if( (subJetCands->at(i).pt()-dau1pt)<0.001 || (subJetCands->at(i).pt()-dau2pt)<0.001){
        if( (subJetCands->at(i).pt()==dau1pt || subJetCands->at(i).pt()==dau2pt) && dau1pt!=0 && dau2pt!=0){
            flag++;
//	    subjet_flavor = subJetCands->at(i).partonFlavor();
	    output->subjet_flavor_ = subJetCands->at(i).partonFlavour();
//          output->subjet_flavor_ = subJetCands->at(i).jetCharge();
//cout<<"subjet flavor: "<<subJetCands->at(i).partonFlavour()<<endl;
            double subjet_discCVS = subJetCands->at(i).bDiscriminator("combinedSecondaryVertexBJetTags");
    	    if(subjet_discCVS>0.244)nsubjetL++;
            if(subjet_discCVS>0.679)nsubjetM++;
            if(subjet_discCVS>0.898)nsubjetT++;
//	    else continue;
//cout<<"size of subjetCollection:"<<subJetCands->size()<<endl;
//cout<<"dex1:"<<dex1<<"    dex2:"<<dex2<<endl;

            if( subJetCands->at(i).pt()==dau1pt && dau1pt!=0) dex1=i;
            if( subJetCands->at(i).pt()==dau2pt && dau2pt!=0) dex2=i;
//cout<<"dex1:"<<dex1<<"    dex2:"<<dex2<<endl;
	}
	else continue;
      }
//cout<<"flag: "<<flag<<endl;
     // dR_subjet = TMath::Sqrt((subJetCands->at(dex1).phi()-subJetCands->at(dex2).phi())*(subJetCands->at(dex1).phi()-subJetCands->at(dex2).phi())+(subJetCands->at(dex1).eta()-subJetCands->at(dex2).eta())*(subJetCands->at(dex1).eta()-subJetCands->at(dex2).eta()));
      if(flag==2){
	subjet1_phi=subJetCands->at(dex1).phi();
        subjet1_eta=subJetCands->at(dex1).eta();
        subjet2_phi=subJetCands->at(dex2).phi();
        subjet2_eta=subJetCands->at(dex2).eta();
      
//cout<<"subjet1 phi:"<<subjet1_phi<<"    subjet1 eta:"<<subjet1_eta<<endl;
//cout<<"subjet2 phi:"<<subjet2_phi<<"    subjet2 eta:"<<subjet2_eta<<endl; 
       dR_subjet = TMath::Sqrt((subjet1_phi-subjet2_phi)*(subjet1_phi-subjet2_phi)+(subjet1_eta-subjet2_eta)*(subjet1_eta-subjet2_eta));
//cout<<"dR_subjet:"<<dR_subjet<<endl;
	output->subjet1_phi_=subjet1_phi;
        output->subjet1_eta_=subjet1_eta;
        output->subjet2_phi_=subjet2_phi;
        output->subjet2_eta_=subjet2_eta;

      	output->dR_subjet_=dR_subjet;
      	output->nsubjetL_=nsubjetL;
      	output->nsubjetM_=nsubjetM;
      	output->nsubjetT_=nsubjetT;

	flag=0;
	}
//cout<<"nsubjetL="<<nsubjetL<<"  nsubjetM="<<nsubjetM<<"  nsubjetT="<<nsubjetT<<endl;
      /*
	std::vector<const reco::Candidate*> candPtrs = pjPtr->getJetConstituentsQuick();
	for(unsigned i=0; i<candPtrs.size(); ++i) {
	const pat::Jet& subjet = pat::Jet(*dynamic_cast<const reco::PFJet*>(&*(candPtrs[i])));
	cmg::PFJet cmgsubjet;
	cmgsubjet.setP4(subjet.p4());
	pfJetFactory_.setPFproperties(subjet,&cmgsubjet, false);
	output->subJetCollection_.push_back(cmgsubjet);
	}//end loop over subjets
	
      */
      
    }//end if we matched a pruned jet to the std one
  }//end if label of pruned jets is not emtpy
  

  delete jecUnc;

}//end set



float cmg::VJetFactory::JetResolution(const edm::Event& iEvent, cmg::VJet *output){
  
  
  bool genjet_match = false;
  float genpt = -10;
  float jetpt = output->pt();
  double factor = 1;
  if(fabs(output->eta())<0.5)      factor = 1.052;
  else if(fabs(output->eta())<1.1) factor = 1.057;
  else if(fabs(output->eta())<1.7) factor = 1.096;
  else if(fabs(output->eta())<2.3) factor = 1.134;
  else                             factor = 1.288;

  edm::Handle<reco::GenJetCollection> GenjetCands;
  iEvent.getByLabel("ca8GenJetsNoNu",GenjetCands);

  double dR = 999;
  for(reco::GenJetCollection::const_iterator genmi = GenjetCands->begin(); genmi != GenjetCands->end(); ++genmi){
    if(deltaR(*output,*genmi) < dR  && deltaR(*output,*genmi) < 0.3){
      dR = deltaR(*output,*genmi);
      genjet_match = true;
      genpt = genmi->pt();
    }
  }

  if(genjet_match){
    jetpt = max(0.,genpt+factor*(jetpt-genpt));
  }
  else{
    double sigmaMC;
    if(fabs(output->eta()) < 0.5 )   sigmaMC = 0.05206; 
    else if(fabs(output->eta())<1.0) sigmaMC = 0.05403;
    else if(fabs(output->eta())<1.5) sigmaMC = 0.06231;
    else if(fabs(output->eta())<2.0) sigmaMC = 0.06452;
    else                             sigmaMC = 0.07672;
    TRandom3 r;
    r.SetSeed(0);
    double resol = sigmaMC;
    double sigma = resol * sqrt(factor*factor-1);
    double smear = r.Gaus(1,sigma);
    jetpt = jetpt*smear;
  }
  
  float smearing_factor = jetpt/output->pt();
  return smearing_factor;
}

