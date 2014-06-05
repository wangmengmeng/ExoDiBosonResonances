#ifndef __AnalyzerEDBR__
#define __AnalyzerEDBR__

#include <Riostream.h>
#include <string>
#include <vector>

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Utilities/interface/Algorithms.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "AnalysisDataFormats/CMGTools/interface/Muon.h"
#include "AnalysisDataFormats/CMGTools/interface/Electron.h"
#include "AnalysisDataFormats/CMGTools/interface/PFJet.h"
#include "AnalysisDataFormats/CMGTools/interface/CompoundTypes.h"
#include "AnalysisDataFormats/ExoDiBosonResonances/interface/CompoundTypesHZZLL.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "AnalysisDataFormats/ExoDiBosonResonances/interface/EDBRCandidate.h"

#include "CommonTools/CandUtils/interface/CenterOfMassBooster.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "CommonTools/CandUtils/interface/cloneDecayTree.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"


#include "TMatrixD.h"
#include "TVectorD.h"
#include "TTree.h"
#include "TFile.h"
#include "TH1F.h"

#include "TVector3.h"
#include "TLorentzVector.h"
using namespace std;


//template <typename T> 
class AnalyzerEDBR : public edm::EDAnalyzer{

 public:
  AnalyzerEDBR(const edm::ParameterSet &ps);


  virtual ~AnalyzerEDBR(){
    cout << "AnalyzerEDBR destructor..." << endl;
    outFile_->cd();
    outTree_->Write();
    outFile_->Close();
  }

  ///Method where the analysis is done.
 
  void beginRun(edm::Run const& iRun, edm::EventSetup const& eventSetup){
    bool aaa;
    hltConfig.init(iRun,eventSetup,"HLT",aaa);
  }

  void endRun(edm::Run const& iRun, edm::EventSetup const& eventSetup){

  }

  void analyze(edm::Event const& iEvent, edm::EventSetup const& eventSetup);
  

  // /// //void analyze(edm::Event const& iEvent, edm::EventSetup const& eventSetup);



 private:
  bool debug_, isMC_,  treatVBFAsMultiple_,saveVBFCands_;            // flags
  std::string cat_;
  std::string outFileName_;
// comment and change for WH
//  std::string VType_;
  std::string VType1_, VType2_;
  std::string cmgEDBRMu_, cmgEDBREle_;
  unsigned int Ngen_;
  double xsec_;
  int VpdgId_; 
// comment and change for WH
//  double VMass_, VTagSFHP_,VTagSFLP_;
  double VMass1_,VMass2_, VTagSFHP_,VTagSFLP_; 
 unsigned int fillGen_;

  void init();
  void initTree();
  void initDataMembers();
  void analyzeTrigger(edm::Event const& iEvent, edm::EventSetup const& eventSetup);
  void analyzeGenLevel(edm::Event const& iEvent, edm::EventSetup const& eventSetup);
  // void analyzeGeneric(edbr,int ih, bool goodKinFit);
  double deltaR(reco::LeafCandidate p1,reco::LeafCandidate p2);
  double deltaR(double phi1,double eta1,double phi2,double eta2);

  //////////////////////////////////////
  /////////////////////////////////////
  //////////////////////////////////////
  /////////////////////////////////////


  template < typename T > void analyzeGeneric(T edbr,int& ih){

 
    //example for the future
    //   if(edbr->getSelection("cuts_btags_btag2")){
    //  btag[ih] = 2;
    // }	

    MCmatch[ih] = edbr->getSelection("cuts_genMatch");
    deltaREDBR[ih] = 0.0;//deltaR(edbr->phi(),edbr->eta(),genEDBR.phi(),genEDBR.eta());




    // if(debug_)cout<<"Inside AnalyzerEDBR::analyzeGeneric "<<ih<<" "<<flush;
    //if(VType_=="W"&&(edbr->leg2().getSelection("cuts_isWSignal"))) reg[ih]=1;
    //if(VType_=="W"&&(edbr->leg2().getSelection("cuts_isWSideband"))) reg[ih]=0;

// comment and change for WH
/*    if(VType_=="Z"){
      if(edbr->leg2().getSelection("cuts_isZSignal"))reg[ih]= 1.0;
      if(edbr->leg2().getSelection("cuts_isZSideband"))reg[ih]= 0.0;
    }
*/
    if(VType2_=="H"){
    if(edbr->leg2().getSelection("cuts_isWSignal"))reg[ih]= 1.0;
    if(edbr->leg2().getSelection("cuts_isWSideband"))reg[ih]= 0.0;
    }
    mzz[ih]=edbr->mass();
    ptmzz[ih]=edbr->pt();
  
    if(debug_)cout<<"Inside AnalyzerEDBR::analyzeGeneric mzz="<<mzz[ih]<<"  pT_mzz="<<ptmzz[ih] <<endl;

    hs[ih]     = edbr->costhetastar();
    h1[ih]     = edbr->helcosthetaZl1();
    h2[ih]     = edbr->helcosthetaZl2();
    phi[ih]    = edbr->helphiZl1();
    phiS1[ih]  = edbr->phistarZl1(); 
    LD[ih] = edbr->userFloat("LD");
  
 

    //   if(debug_)cout<<"AnalyzerEDBR::analyzeGeneric filling mLL" <<endl;
    mll[ih]=edbr->leg1().mass();
 
    ptZll[ih]=edbr->leg1().pt();
    ptZjj[ih]=edbr->leg2().pt();
    yZll[ih]=edbr->leg1().rapidity();
    yZjj[ih]=edbr->leg2().rapidity();
    phiZll[ih]=edbr->leg1().phi();
    phiZjj[ih]=edbr->leg2().phi();

    //   if(debug_)cout<<"AnalyzerEDBR::analyzeGeneric filling leptons" <<endl;

    bool highptLep1=true;
    if(edbr->leg1().leg2().pt()>edbr->leg1().leg1().pt())highptLep1=false;
// change for WH
//    if(VType_=="W")highptLep1=true;//for ww case, we don't compare pt of lepton and neutrino
    if(VType1_=="W")highptLep1=true;//for ww case, we don't compare pt of lepton and neutrino   
    if(highptLep1){
      ptlep1[ih]=edbr->leg1().leg1().pt();
      ptlep2[ih]=edbr->leg1().leg2().pt();
      etalep1[ih]=edbr->leg1().leg1().eta();
      etalep2[ih]=edbr->leg1().leg2().eta();
      philep1[ih]=edbr->leg1().leg1().phi();
      philep2[ih]=edbr->leg1().leg2().phi();
      isolep1[ih]=edbr->leg1().leg1().relIso();
      isolep2[ih]=edbr->leg1().leg2().relIso();
    }
    else{
      ptlep1[ih]=edbr->leg1().leg2().pt();
      ptlep2[ih]=edbr->leg1().leg1().pt();
      etalep1[ih]=edbr->leg1().leg2().eta();
      etalep2[ih]=edbr->leg1().leg1().eta();
      philep1[ih]=edbr->leg1().leg2().phi();
      philep2[ih]=edbr->leg1().leg1().phi();
      isolep1[ih]=edbr->leg1().leg2().relIso();
      isolep2[ih]=edbr->leg1().leg1().relIso();
    }


    deltaRleplep[ih]=deltaR(edbr->leg1().leg1().phi(),
			    edbr->leg1().leg1().eta(),
			    edbr->leg1().leg2().phi(),
			    edbr->leg1().leg2().eta());

    mt[ih] = sqrt( 2*edbr->leg1().leg1().pt()*edbr->leg1().leg2().pt()*( 1-cos(edbr->leg1().leg1().phi()-edbr->leg1().leg2().phi()) ) );
    nbtagsL[ih] = edbr->userFloat("nbtagsL");
    nbtagsM[ih] = edbr->userFloat("nbtagsM");
    nbtagsT[ih] = edbr->userFloat("nbtagsT");
    nbtagscleanL[ih] = edbr->userFloat("nbtagscleanL"); 
    nbtagscleanM[ih] = edbr->userFloat("nbtagscleanM"); 
    nbtagscleanT[ih] = edbr->userFloat("nbtagscleanT"); 
  

    //if(finalM_||sbM_||finalE_||sbE_){//with this if condition, presel will have PU weights==1

    // THESE WEIGHTS=1 FOR REAL DATA
    HLTSF = edbr->userFloat("HLTWeight");
// comment and change for WH
//	if(VType_=="W")BTagWeight = edbr->userFloat("BTagWeight");
        if(VType2_=="H")BTagWeight = edbr->userFloat("BTagWeight");
	else BTagWeight =1.0;
    if(edbr->hasUserFloat("PUWeights")){
      //if(preselM_ || preselM1J_ ||preselE_ ||preselE1J_ ){
      //   std::cout<<"Event passes presel path"<<std::endl;
      PU  = edbr->userFloat("PUWeights");
      PUA = edbr->userFloat("PUWeights2012A");
      PUB = edbr->userFloat("PUWeights2012B");
    }
    else if(edbr->hasUserFloat("PUWeightsFullE")){
      //else if( finalE_ || sbE_|| finalE1J_ || sbE1J_){   
      if(!elePath_)std::cout<<"Warning from AnalyzerEDBR::analyzeGeneric Run "<<run<<" Event "<<nevent<<" : EDBR cand  has userfloat PUWeightsFullE but elePath_==false . This could be an indication of something not properly right."<<std::endl;
     
      PU  = edbr->userFloat("PUWeightsFullE");
      PUA = edbr->userFloat("PUWeights2012AFullE");
      PUB = edbr->userFloat("PUWeights2012BFullE");
    }
    else if(edbr->hasUserFloat("PUWeightsFullM")){
      //else if( finalM_ || sbM_|| finalM1J_ || sbM1J_){
     
      if(!muPath_)std::cout<<"Warning from AnalyzerEDBR::analyzeGeneric Run "<<run<<" Event "<<nevent<<" : EDBR cand  has userfloat PUWeightsFullM but muPath_==false . This could be an indication of something not properly right."<<std::endl;
      PU  = edbr->userFloat("PUWeightsFullM");
      PUA = edbr->userFloat("PUWeights2012AFullM");
      PUB = edbr->userFloat("PUWeights2012BFullM");
    }
    else{
      PU  = -99.0;
      PUA = -99.0;
      PUB = -99.0;
    }
   
    //  if(debug_)cout<<"AnalyzerEDBR::analyzeGeneric finishing Cand #" <<ih<<endl;
  
  }//end analyzeGeneric

  //////////////////////////////////////
  /////////////////////////////////////
  //////////////////////////////////////
  /////////////////////////////////////



  template < typename T > void  CalculateMWW(T edbr,int& ih,int lepType){

// comment and change for WH
//    double MW_=VMass_;
    double MW1_=VMass1_;
//    double MW2_=VMass2_; // no use for WH

    double leppt = edbr->leg1().leg1().pt();
    double lepphi = edbr->leg1().leg1().phi();
    double lepeta = edbr->leg1().leg1().eta();

    double metpt = edbr->leg1().leg2().pt();
    double metphi = edbr->leg1().leg2().phi();

    double  pxj= edbr->leg2().px();
    double  pyj= edbr->leg2().py();
    double  pzj= edbr->leg2().pz();
    double  Ej = edbr->leg2().energy();	

    double	px = metpt*cos(metphi);
    double	py = metpt*sin(metphi);
    double  pz = 0;
    double	pxl= leppt*cos(lepphi);
    double	pyl= leppt*sin(lepphi);
    double	pzl= leppt*sinh(lepeta);
    double	El = edbr->leg1().leg1().energy();
// comment and change for WH
//    double	a = pow(MW_,2) + pow(px+pxl,2) + pow(py+pyl,2) - px*px - py*py - El*El + pzl*pzl;
    double    a = pow(MW1_,2) + pow(px+pxl,2) + pow(py+pyl,2) - px*px - py*py - El*El + pzl*pzl;
    double	b = 2.*pzl;   
    double	A = b*b -4.*El*El;
    double	B = 2.*a*b;
    double	C = a*a-4.*(px*px+py*py)*El*El;

    TLorentzVector lepP4(pxl,pyl,pzl,El);
    TLorentzVector jetP4(pxj,pyj,pzj,Ej);
    TLorentzVector neuP4;
    TLorentzVector neuP4_ptUncorrected;
    ///////////////////////////pz for fnal
    double M_mu =  0; 
    if(lepType==1)M_mu=0.105658367;//mu
    if(lepType==0)M_mu=0.00051099891;//electron

    //    double otherSol_ = 0.; 
// comment and change for WH
//    a = MW_*MW_ - M_mu*M_mu + 2.0*pxl*px + 2.0*pyl*py;
    a = MW1_*MW1_ - M_mu*M_mu + 2.0*pxl*px + 2.0*pyl*py;
    A = 4.0*(El*El - pzl*pzl);
    B = -4.0*a*pzl;
    C = 4.0*El*El*(px*px + py*py) - a*a;

    double newPtneutrino_=0;
    double tmproot = B*B - 4.0*A*C;

    if (tmproot<0) {
      pz = - B/(2*A); // take real part of complex roots
      // double otherSol_ = pz;

      // recalculate the neutrino pT
      // solve quadratic eq. discriminator = 0 for pT of nu
      double pnu = metpt;
// comment and change for WH
//      double Delta = (MW_*MW_ - M_mu*M_mu);
      double Delta = (MW1_*MW1_ - M_mu*M_mu);
      double alpha = (pxl*px/pnu + pyl*py/pnu);
      double AA = 4.*pzl*pzl - 4*El*El + 4*alpha*alpha;//note this is alwawys <0
      double BB = 4.*alpha*Delta;
      double CC = Delta*Delta;//note this is always >0

      double tmpdisc = BB*BB - 4.0*AA*CC; // always >0, and one root positive, one root negative
      double tmpsolpt1 = (-BB + TMath::Sqrt(tmpdisc))/(2.0*AA);
      double tmpsolpt2 = (-BB - TMath::Sqrt(tmpdisc))/(2.0*AA);

      //reject negative root
      if(tmpsolpt1<0)newPtneutrino_=tmpsolpt2;
      else newPtneutrino_=tmpsolpt1;
      //save pz
      pz_type0[ih]=pz_type1[ih]=pz_type2[ih]=pz_type3[ih]=pz_type4[ih]=pz;
      //save mWW
      //new pt	
      double neu_pt = newPtneutrino_;
      pt_neutrino_corrected[ih] = newPtneutrino_;
      neuP4.SetPxPyPzE(neu_pt* cos(metphi), neu_pt * sin(metphi), pz, sqrt(neu_pt*neu_pt + pz*pz) );
      //old pt
      neu_pt = metpt;
      pt_neutrino[ih]=metpt;
      neuP4_ptUncorrected.SetPxPyPzE(neu_pt* cos(metphi), neu_pt * sin(metphi), pz, sqrt(neu_pt*neu_pt + pz*pz) );
      mZZ_type0[ih]=mZZ_type1[ih]=mZZ_type2[ih]=mZZ_type3[ih]=mZZ_type4[ih]=(lepP4+neuP4+jetP4).M();
      mZZ_type0_ptUncorrected[ih]=mZZ_type1_ptUncorrected[ih]=mZZ_type2_ptUncorrected[ih]=mZZ_type3_ptUncorrected[ih]=mZZ_type4_ptUncorrected[ih]=(lepP4+neuP4_ptUncorrected+jetP4).M();
    }
    else {
      //double otherSol_ = 0.; 
      double tmpsol1 = (-B + TMath::Sqrt(tmproot))/(2.0*A);
      double tmpsol2 = (-B - TMath::Sqrt(tmproot))/(2.0*A);
      pt_neutrino[ih]=pt_neutrino_corrected[ih]=metpt;
      //std::cout << " Neutrino Solutions: " << tmpsol1 << ", " << tmpsol2 << std::endl;
      for(int type=0;type<=4;type++)
	{
	  if (type == 0 ) {
	    // two real roots, pick the one closest to pz of muon
	    if (TMath::Abs(tmpsol2-pzl) < TMath::Abs(tmpsol1-pzl)) { pz = tmpsol2; }//otherSol_ = tmpsol1;
	    else { pz = tmpsol1; }// otherSol_ = tmpsol2;
	    // if pz is > 300 pick the most central root
	    if ( abs(pz) > 300. ) {
	      if (TMath::Abs(tmpsol1)<TMath::Abs(tmpsol2) ) { pz = tmpsol1; }// otherSol_ = tmpsol2;
	      else { pz = tmpsol2; } // otherSol_ = tmpsol1;
	    }
	    pz_type0[ih]=pz;
	    neuP4.SetPxPyPzE(px,py,pz,sqrt(px*px+py*py+pz*pz));
	    mZZ_type0[ih]=mZZ_type0_ptUncorrected[ih]=(lepP4+neuP4+jetP4).M();
	  }
	  if (type == 1 ) {
	    // two real roots, pick the one closest to pz of muon
	    if (TMath::Abs(tmpsol2-pzl) < TMath::Abs(tmpsol1-pzl)) { pz = tmpsol2; }// otherSol_ = tmpsol1;
	    else {pz = tmpsol1; }// otherSol_ = tmpsol2;
	    pz_type1[ih]=pz;
            neuP4.SetPxPyPzE(px,py,pz,sqrt(px*px+py*py+pz*pz));
            mZZ_type1[ih]=mZZ_type1_ptUncorrected[ih]=(lepP4+neuP4+jetP4).M();
	  }
	  if (type == 2 ) {
	    // pick the most central root.
	    if (TMath::Abs(tmpsol1)<TMath::Abs(tmpsol2) ) { pz = tmpsol1;} // otherSol_ = tmpsol2; 
	    else { pz = tmpsol2; }// otherSol_ = tmpsol1;
	    pz_type2[ih]=pz;
            neuP4.SetPxPyPzE(px,py,pz,sqrt(px*px+py*py+pz*pz));
            mZZ_type2[ih]=mZZ_type2_ptUncorrected[ih]=(lepP4+neuP4+jetP4).M();
	  }
	  if (type == 3 ) {
	    // pick the largest value of the cosine
	    TVector3 p3w, p3mu;
	    p3w.SetXYZ(pxl+px, pyl+py, pzl+ tmpsol1);
	    p3mu.SetXYZ(pxl, pyl, pzl );
// comment and change for WH
//            double sinthcm1 = 2.*(p3mu.Perp(p3w))/MW_;
	    double sinthcm1 = 2.*(p3mu.Perp(p3w))/MW1_;
	    p3w.SetXYZ(pxl+px, pyl+py, pzl+ tmpsol2);
//	    double sinthcm2 = 2.*(p3mu.Perp(p3w))/MW_;
            double sinthcm2 = 2.*(p3mu.Perp(p3w))/MW1_;

	    double costhcm1 = TMath::Sqrt(1. - sinthcm1*sinthcm1);
	    double costhcm2 = TMath::Sqrt(1. - sinthcm2*sinthcm2);

	    if ( costhcm1 > costhcm2 ) { pz = tmpsol1;} // otherSol_ = tmpsol2; 
	    else { pz = tmpsol2; }//otherSol_ = tmpsol1;
	    pz_type3[ih]=pz;
            neuP4.SetPxPyPzE(px,py,pz,sqrt(px*px+py*py+pz*pz));
            mZZ_type3[ih]=mZZ_type3_ptUncorrected[ih]=(lepP4+neuP4+jetP4).M();
	  }//end of type3
	  if (type == 4 ) {
	    // pick the larger abs root.
	    if (TMath::Abs(tmpsol1)>TMath::Abs(tmpsol2) ) { pz = tmpsol1; }// otherSol_ = tmpsol2;
	    else { pz = tmpsol2; }// otherSol_ = tmpsol1;
	    pz_type4[ih]=pz;
            neuP4.SetPxPyPzE(px,py,pz,sqrt(px*px+py*py+pz*pz));
            mZZ_type4[ih]=mZZ_type4_ptUncorrected[ih]=(lepP4+neuP4+jetP4).M();
	  }//endl of type4
	  
	}//endl of loop over type
    }//endl of if real root

  }


  //functions specific for boosted and not-boosted topologies  
  template < typename T > void  analyzeSingleJet(T edbr,int& ih){
    //  if(debug_)cout<<"AnalyzerEDBR::analyzeSingleJet filling jet vars  " <<ih<<endl;

    if(debug_)std::cout<<"nXJets="<<edbr->userFloat("nXJets")<<" (it should be ==1) "<<endl;
    nXjets[ih]=1;//edbr->nJets();
    mzzNoKinFit[ih]=edbr->mass();
    mjj[ih]=edbr->leg2().prunedMass();
    mjjNoKinFit[ih]=mjj[ih];
//comment and change for WH
/*    //40-65 -- 65-105 -- 105-130
    if(VType_=="W"&&(mjjNoKinFit[ih]>65&&mjjNoKinFit[ih]<105)) reg[ih]=1;
    else if(VType_=="W"&&( (mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65) || (mjjNoKinFit[ih]>105&&mjjNoKinFit[ih]<130)) ) reg[ih]=0;
    else if(VType_=="W") reg[ih]=-1;
*/
    if(VType2_=="H"&&(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<135)) reg[ih]=1;
//    if(VType2_=="H"&&(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<140)) reg[ih]=1;
    else if(VType2_=="H"&&( (mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65)) ) reg[ih]=0;
//    else if(VType2_=="H"&& ((mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65)||(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<135))) reg[ih]=-1;
//    else if(VType2_=="H"&& ((mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65)||(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<140))) reg[ih]=-1;
    else if(VType2_=="H")  reg[ih]=-1;
    ptmzzNoKinFit[ih]=edbr->pt();
    ptjjNoKinFit[ih]=edbr->leg2().pt();
    ////fill jet kine vars: first jet vars refer to jet used for building EDBR,
    ////                    second jet vars are dummy
 
    bool highptJet1=true;
    if(highptJet1){
      ptjet1[ih]=edbr->leg2().pt();
      ptjet2[ih]=-99.0;
      etajet1[ih]=edbr->leg2().eta();
      etajet2[ih]=-99.0;
      phijet1[ih]=edbr->leg2().phi();
      phijet2[ih]=-99.0;
      massjet1[ih]=edbr->leg2().mass();
      massjet2[ih]=-99.0;
      
      betajet1[ih] = edbr->leg2().beta(); 
      betajet2[ih] = -1.0;
      puMvajet1[ih] = edbr->leg2().puMva("full"); 
      puMvajet2[ih] = -9999.0;
    }

    deltaRjetjet[ih]=0.0;

    //jet sub-structure 
    prunedmass[ih]=edbr->leg2().prunedMass();
    mdrop[ih]=edbr->leg2().mdrop();
    qjet[ih]= edbr->leg2().qjet();
    nsubj21[ih]=edbr->leg2().ntau21();
    nsubj32[ih]=edbr->leg2().ntau32();
    tau1[ih]=edbr->leg2().tau1();
    tau2[ih]=edbr->leg2().tau2();
// add tau3/4/5 etc.
    tau3[ih]=edbr->leg2().tau3();
    tau4[ih]=edbr->leg2().tau4();
    tau5[ih]=edbr->leg2().tau5();
    nsubj31[ih]=edbr->leg2().ntau31();
    nsubj41[ih]=edbr->leg2().ntau41();
    nsubj51[ih]=edbr->leg2().ntau51();
    nsubj42[ih]=edbr->leg2().ntau42();
    nsubj52[ih]=edbr->leg2().ntau52();
    nsubj43[ih]=edbr->leg2().ntau43();
    nsubj53[ih]=edbr->leg2().ntau53();
    nsubj54[ih]=edbr->leg2().ntau54();
// add fat & sub b jet here for WH
    nfatjetbtagL[ih]=edbr->leg2().nfatjetL();
    nfatjetbtagM[ih]=edbr->leg2().nfatjetM();
    nfatjetbtagT[ih]=edbr->leg2().nfatjetT();

    nsubjetbtagL[ih]=edbr->leg2().nsubjetL();
    nsubjetbtagM[ih]=edbr->leg2().nsubjetM();
    nsubjetbtagT[ih]=edbr->leg2().nsubjetT();
    dR_subjet[ih]=edbr->leg2().dR_subjet();
    subjet1_phi[ih]=edbr->leg2().subjet1_phi();
    subjet1_eta[ih]=edbr->leg2().subjet1_eta();
    subjet2_phi[ih]=edbr->leg2().subjet2_phi();
    subjet2_eta[ih]=edbr->leg2().subjet2_eta();
    subjet_flavor[ih]=edbr->leg2().subjet_flavor();

    double nsubjcut=0.5;
// comment and change for WH
//    if(VType_=="W") nsubjcut=0.5;
    if(VType2_=="H") nsubjcut=0.5;
    if(nsubj21[ih]<nsubjcut) vTagPurity[ih]=1.0;
    else if(nsubj21[ih]<0.75) vTagPurity[ih]=0.0;
    else  vTagPurity[ih]=-1.0;
	
	if(vTagPurity[ih]==1) vtagw=VTagSFHP_;
	else if(vTagPurity[ih]==0) vtagw=VTagSFLP_;
	else vtagw=1;

    //( edbr->getSelection("tag_SingleJetHP")? 1.0 : 0.0 );
    // nsubj21[ih]<0.45 -> 1.0  //nsubj21[ih]>0.45 &&  nsubj21[ih]<0.75 -> 0.0


    btagjet1[ih]=edbr->leg2().bDiscriminator( "combinedSecondaryVertexBJetTags" );
    // these are dummy
    btagjet2[ih]=-99.0;
    q1fl[ih]=-99.0;
    q2fl[ih]=-99.0;
    qgjet1[ih]=-99.0;
    qgjet2[ih]=-99.0;
    qgProduct[ih]=-99.0;

	TOBTECjetsId[ih]=edbr->leg2().getSelection("cuts_TOBTECjetsId");
  }//end analyzeSingleJet();


  template < typename T > void  analyzeDoubleJet(T edbr,int& ih, bool & goodKinFit){

// comment and change for WH
//    if(edbr->leg2().mass()<VMass_-1 ||edbr->leg2().mass()>VMass_+1){
    if(edbr->leg2().mass()<VMass2_-1 ||edbr->leg2().mass()>VMass2_+1){
      cout<<"WARNING from AnalyzeEDBR::analyzeDoubleJet : KIN FIT badly converged!! M_jj="<<edbr->leg2()<<endl;
      goodKinFit = false;
    }

    if(debug_)std::cout<<"nXJets="<<edbr->userFloat("nXJets")<<" (it should be ==2) "<<endl;
    nXjets[ih]=int(edbr->userFloat("nXJets"));//edbr->nJets();
    vTagPurity[ih]=-2.0;//dummy for 2-Jet topology
    mzzNoKinFit[ih]=edbr->userFloat("nokinfitMZZ");
    ptmzzNoKinFit[ih]=edbr->userFloat("nokinfitPTZZ");
    mjj[ih]=edbr->leg2().mass();
    mjjNoKinFit[ih]=edbr->userFloat("nokinfitMJJ");
// comment and change for WH
/*    if(VType_=="W"&&(mjjNoKinFit[ih]>65&&mjjNoKinFit[ih]<105)) reg[ih]=1;
    else if(VType_=="W"&&( (mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65) || (mjjNoKinFit[ih]>105&&mjjNoKinFit[ih]<130)) ) reg[ih]=0;
    else if(VType_=="W") reg[ih]=-1;
*/
    if(VType2_=="H"&&(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<135)) reg[ih]=1;
//    if(VType2_=="H"&&(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<140)) reg[ih]=1;
    else if(VType2_=="H"&&( (mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65)) ) reg[ih]=0;
//    else if(VType2_=="H"&& ((mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65)||(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<135))) reg[ih]=-1;
//    else if(VType2_=="H"&& ((mjjNoKinFit[ih]>40&&mjjNoKinFit[ih]<65)||(mjjNoKinFit[ih]>110&&mjjNoKinFit[ih]<140))) reg[ih]=-1;
    else if(VType2_=="H")  reg[ih]=-1;

    //  double isomu1mod[nMaxCand], isomu2mod[nMaxCand]; // modified tracker iso for muons
    //  double isoele1trk[nMaxCand], isoele2trk[nMaxCand], isoele1calo[nMaxCand], isoele2calo[nMaxCand]; // modified isos for ele

    ptjjNoKinFit[ih]=edbr->userFloat("nokinfitPTJJ");
    etajjNoKinFit[ih]=edbr->userFloat("nokinfitEtaJJ");
    phijjNoKinFit[ih]=edbr->userFloat("nokinfitPhiJJ");
    if(debug_)cout<<"AnalyzerEDBR::analyzeDoubleJet filling jet vars  " <<ih<<endl;
    ////fill jet kine vars
    bool highptJet1=true;
    if(edbr->leg2().leg2().pt()>edbr->leg2().leg1().pt())highptJet1=false;
    if(highptJet1){
      ptjet1[ih]=edbr->leg2().leg1().pt();
      ptjet2[ih]=edbr->leg2().leg2().pt();
      etajet1[ih]=edbr->leg2().leg1().eta();
      etajet2[ih]=edbr->leg2().leg2().eta();
      phijet1[ih]=edbr->leg2().leg1().phi();
      phijet2[ih]=edbr->leg2().leg2().phi();
      massjet1[ih]=edbr->leg2().leg1().mass();
      massjet2[ih]=edbr->leg2().leg2().mass();
      

      betajet1[ih] = edbr->leg2().leg1().beta(); 
      betajet2[ih] = edbr->leg2().leg2().beta(); 
      puMvajet1[ih] = edbr->leg2().leg1().puMva("full"); 
      puMvajet2[ih] = edbr->leg2().leg2().puMva("full"); 

      btagjet1[ih]=edbr->leg2().leg1().bDiscriminator( "combinedSecondaryVertexBJetTags" );
      btagjet2[ih]=edbr->leg2().leg2().bDiscriminator( "combinedSecondaryVertexBJetTags" );

    }
    else{
      ptjet2[ih]=edbr->leg2().leg1().pt();
      ptjet1[ih]=edbr->leg2().leg2().pt();
      etajet2[ih]=edbr->leg2().leg1().eta();
      etajet1[ih]=edbr->leg2().leg2().eta();
      phijet2[ih]=edbr->leg2().leg1().phi();
      phijet1[ih]=edbr->leg2().leg2().phi();

      betajet2[ih] = edbr->leg2().leg1().beta(); 
      betajet1[ih] = edbr->leg2().leg2().beta(); 
      puMvajet2[ih] = edbr->leg2().leg1().puMva("full"); 
      puMvajet1[ih] = edbr->leg2().leg2().puMva("full");

      btagjet2[ih]=edbr->leg2().leg1().bDiscriminator( "combinedSecondaryVertexBJetTags" );
      btagjet1[ih]=edbr->leg2().leg2().bDiscriminator( "combinedSecondaryVertexBJetTags" );

    }

    deltaRjetjet[ih]=deltaR(edbr->leg2().leg1().phi(),
			    edbr->leg2().leg1().eta(),
			    edbr->leg2().leg2().phi(),
			    edbr->leg2().leg2().eta());

    //jet sub-structure is dummy for double jet
    //jet sub-structure 
    prunedmass[ih]=-99.0;
    mdrop[ih]=-999.0;
    qjet[ih]=-999.0;
    nsubj21[ih]=-999.0;
    nsubj32[ih]=-999.0;
    tau1[ih]=-999.0;
    tau2[ih]=-999.0;
// add tau3/4/5 etc.
    tau3[ih]=-999.0;
    tau4[ih]=-999.0;
    tau5[ih]=-999.0;
    nsubj31[ih]=-999.0;
    nsubj41[ih]=-999.0;
    nsubj51[ih]=-999.0;
    nsubj42[ih]=-999.0;
    nsubj52[ih]=-999.0;
    nsubj43[ih]=-999.0;
    nsubj53[ih]=-999.0;
    nsubj54[ih]=-999.0;  
// add fat & sub b jet here for WH
    nfatjetbtagL[ih]=-999.0;
    nfatjetbtagM[ih]=-999.0;
    nfatjetbtagT[ih]=-999.0;

    nsubjetbtagL[ih]=-999.0;
    nsubjetbtagM[ih]=-999.0;
    nsubjetbtagT[ih]=-999.0;
  
    subjet_flavor[ih]=30; 
    dR_subjet[ih]=10.0;
    subjet1_phi[ih]=10.0;
    subjet1_eta[ih]=10.0;
    subjet2_phi[ih]=10.0;
    subjet2_eta[ih]=10.0;
    //these are dummy

    q1fl[ih]=-99.0;
    q2fl[ih]=-99.0;
    qgjet1[ih]=-99.0;
    qgjet2[ih]=-99.0;
    qgProduct[ih]=-99.0;


  
    //  if(finalM_||sbM_||finalE_||sbE_){
    //  if(readQGFromUserFloat_) qgProduct[ih] = edbr->userFloat("QG");
    //  else {  // pandolfi to be blamed for this
    //    edm::ProductID prodId = edbr->leg2().leg2().sourcePtr()->id(); //should be the same for both legs
    //    size_t index1 = edbr->leg2().leg1().sourcePtr()->key();
    //    size_t index2 = edbr->leg2().leg2().sourcePtr()->key();
    //    
    //    // QG LIKELIHOOD FROM JETS
    //    qgProduct[ih] = qgmap->get(prodId,index2) * qgmap->get(prodId,index1);
    //    if(edbr->leg2().leg1().pt()>edbr->leg2().leg2().pt()){
    //	qgjet1[ih] = qgmap->get(prodId,index1);
    //	qgjet2[ih] = qgmap->get(prodId,index2);
    //    } else {
    //	qgjet1[ih] = qgmap->get(prodId,index2);
    //	qgjet2[ih] = qgmap->get(prodId,index1);
    //   }
    //  }// end else recalculate qgProd
    //  }//end if finalM_||sbM_||finalE_||sbE_
 

  }//end analyzeDoubleJet();


  //////////////////////////////////////
  /////////////////////////////////////
  //functions specific for lepton flavors
  // void analyzeMuon(edm::RefToBase<cmg::DiMuonDiJetEDBR > edbr, int ih);
  template < typename T > void  analyzeMuon(T edbr, int ih){
    //nothing to be done
    //
    //
    if(debug_)cout<<"Inside AnalyzerEDBR::analyzeMuon"<<endl;

    lep[ih]=1;
    isomu1mod[ih]=edbr->userFloat("isomu1mod");
    isomu2mod[ih]=edbr->userFloat("isomu2mod");

    /// Let's add the muon ID here for Shuai!
    /*
      const pat::Muon* patMuonPtr = edbr->leg1().leg1().sourcePtr()->get();
      const reco::Track* globalTrackPtr = patMuonPtr->globalTrack();
      const reco::Track* innerTrackPtr = patMuonPtr->innerTrack();
      int isGlobalMuon     = patMuonPtr->isGlobalMuon() ? 1 : 0;
      int numTrackerLayers = innerTrackPtr->hitPattern().trackerLayersWithMeasurement();
      int numPixelHits     = innerTrackPtr->hitPattern().numberOfValidPixelHits();
      int numMuonHits      = globalTrackPtr->hitPattern().numberOfValidMuonHits();
      int numMatches       = patMuonPtr->numberOfMatchedStations();
    */
    /// Easier life...
    const cmg::Muon& cmgMuon = edbr->leg1().leg1();
    int isGlobalMuon     = cmgMuon.isGlobalMuon() ? 1 : 0;
    int numTrackerLayers = cmgMuon.trackerLayersWithMeasurement();
    int numPixelHits     = cmgMuon.numberOfValidPixelHits();
    int numMuonHits      = cmgMuon.numberOfValidMuonHits();
    int numMatches       = cmgMuon.numberOfMatches();
    double dXY           = fabs(cmgMuon.dxy());
    double dZ            = fabs(cmgMuon.dz());

    globalMuon[ih] = isGlobalMuon;
    nTrackerLayers[ih] = numTrackerLayers;
    nPixelHits[ih] = numPixelHits;
    nMuonHits[ih] = numMuonHits;
    nMatches[ih] = numMatches;
    muondXY[ih] = dXY;
    muondZ[ih] = dZ;

    //dummy for muons 
    eleMVAId1[ih] = -1.0;
    eleMVAId2[ih] = -1.0;

  }//end analyzeMuon


  template < typename T > void analyzeElectron(T edbr, int ih){


    if(debug_)cout<<"Inside AnalyzerEDBR::analyzeElectron for cand#"<<ih<<" : "<<std::flush;
    bool highptLep1=true;
    if(edbr->leg1().leg2().pt()>edbr->leg1().leg1().pt())highptLep1=false;
//comment and change for WH
//    if(VType_=="W")highptLep1=true;//for ww case, we don't compare pt of lepton and neutrino
    if(VType1_=="W")highptLep1=true;//for ww case, we don't compare pt of lepton and neutrino
    lep[ih]=0;    
   
    isoele1trk[ih]=edbr->userFloat("isoele1trk");
    isoele2trk[ih]=edbr->userFloat("isoele2trk");
    isoele1calo[ih]=edbr->userFloat("isoele1calo");
    isoele2calo[ih]=edbr->userFloat("isoele2calo");
 
    if(highptLep1){
      eleMVAId1[ih] = edbr->leg1().leg1().mvaTrigV0(); 
      eleMVAId2[ih] = edbr->leg1().leg2().mvaTrigV0();
    } 
    else{
      eleMVAId1[ih] = edbr->leg1().leg2().mvaTrigV0(); 
      eleMVAId2[ih] = edbr->leg1().leg1().mvaTrigV0();
    }

    //electron id variables
    sigmaIetaIeta[ih]=edbr->leg1().leg1().sigmaIetaIeta();
    deltaPhiSuperClusterTrackAtVtx[ih]=edbr->leg1().leg1().deltaPhiSuperClusterTrackAtVtx();
    deltaEtaSuperClusterTrackAtVtx[ih]=edbr->leg1().leg1().deltaEtaSuperClusterTrackAtVtx();
    hadronicOverEm[ih]=edbr->leg1().leg1().hadronicOverEm();
    numberOfHits[ih]=edbr->leg1().leg1().numberOfHits();
    dxy[ih]=edbr->leg1().leg1().dxy();
    dz[ih]=edbr->leg1().leg1().dz(); 
    ecalDriven[ih]=edbr->leg1().leg1().ecalDriven();
    convDist[ih]=edbr->leg1().leg1().convDist();
    convDcot[ih]=edbr->leg1().leg1().convDcot();
    isConv[ih]=edbr->leg1().leg1().isConv();
    passConversionVeto[ih]=edbr->leg1().leg1().passConversionVeto();
	
    /*
      cout<<"missing hits: "<<edbr->leg1().leg1().sourcePtr()->get()->gsfTrack().get()->trackerExpectedHitsInner().numberOfLostHits()<<endl;
      cout<<"e2x5Max: "<<edbr->leg1().leg1().sourcePtr()->get()->e2x5Max()<<endl;
      cout<<"e5x5: "<<edbr->leg1().leg1().sourcePtr()->get()->e5x5()<<endl;
    */
	
    numberOfLostHits[ih]=edbr->leg1().leg1().sourcePtr()->get()->gsfTrack().get()->trackerExpectedHitsInner().numberOfLostHits();
    e1x5[ih]=edbr->leg1().leg1().sourcePtr()->get()->e1x5();
    e2x5Max[ih]=edbr->leg1().leg1().sourcePtr()->get()->e2x5Max();
    e5x5[ih]=edbr->leg1().leg1().sourcePtr()->get()->e5x5();
    e1x5Over5x5[ih] = (e5x5[ih]!=0 ? e1x5[ih]/e5x5[ih] : 0.);
    e2x5MaxOver5x5[ih] = (e5x5[ih]!=0 ? e2x5Max[ih]/e5x5[ih] : 0.);

    // Muon ID variables are dummy for electrons
    globalMuon[ih] = -1;
    nTrackerLayers[ih] = -1;
    nPixelHits[ih] = -1;
    nMuonHits[ih] = -1;
    nMatches[ih] = -1;
    muondXY[ih] = -1;
    muondZ[ih] = -1;
	
    if(debug_)    std::cout<<"leg1.eleMVA="<<eleMVAId1[ih]<<"  leg2.eleMVA="<<eleMVAId2[ih]<<std::endl;
	
  }//end analyzeElectron


  template < typename T > int checkVBFTag(T edbr,int ih,bool vbfFound, bool& keepThisVBFCand){
  
    int vbfFlag=0;//not a VBF-tagged candidate by default
    if(edbr->vbfptr().isAvailable() )vbfFlag = 1;
    //if(edbr->getSelection("tag_vbfDoubleJet_vbf") || edbr->getSelection("tag_vbfSingleJet_vbf")  )vbfFlag = 1;
         
    if(!treatVBFAsMultiple_){//save only 1st VBF, skip all other vbf combinations associated to the same cand
      if(ih>0){//don't even bother if this is the very first candidate
	if(vbfFlag>0 && vbfFound  ){//this cand is vbf tagged and we have already found another vbf-tagged
	  
	  for(int tmpInd1=0;tmpInd1<ih;tmpInd1++){
	    if(VBFTag[tmpInd1]>0){
	      double mdiffTmp=edbr->mass()-mzz[tmpInd1];
	      if(mdiffTmp<0.01)keepThisVBFCand=false;
	    }
	  }//end loop on previous candidates
	}
      }//end if ih>0
    }//end if !treatVBFAsMultiple_
    
 
    return vbfFlag;
  }//end checkVBFTag

  template < typename T > void analyzeVBF(T edbr,int ih,int vbfFlag){

    VBFmJJ[ih]=-777.0;
    VBFdeltaEta[ih]=-777.0;
    VBFptjet1[ih]=-777.0;
    VBFptjet2[ih]=-777.0;
    VBFetajet1[ih]=-777.0;
    VBFetajet2[ih]=-777.0;
    VBFphijet1[ih]=-777.0;
    VBFphijet2[ih]=-777.0;

    if(vbfFlag>0){
      VBFmJJ[ih]=edbr->vbfptr()->mass();
      VBFptjet1[ih]=edbr->vbfptr()->leg1().pt();
      VBFptjet2[ih]=edbr->vbfptr()->leg2().pt();
      VBFetajet1[ih]=edbr->vbfptr()->leg1().eta();
      VBFetajet2[ih]=edbr->vbfptr()->leg2().eta();
      VBFphijet1[ih]=edbr->vbfptr()->leg1().phi();
      VBFphijet2[ih]=edbr->vbfptr()->leg2().phi();
      VBFdeltaEta[ih]=fabs(VBFetajet1[ih]-VBFetajet2[ih]);
    }

  }//end analyzeVBF

   //////////////////////////////////////
   // DATA MEMBERS


  edm::InputTag XEEColl_,XEELDMap_,XEEJColl_,XEEJLDMap_;
  edm::InputTag XMMColl_,XMMLDMap_,XMMJColl_,XMMJLDMap_;
  edm::InputTag  XQGMap_;

  const static int nMaxCand = 30;
  const static int nMaxTrig = 20;
  //  int nCands_;

  const static int metSignMax = 10;

  /// variables to be stored in the output tree
  TTree* outTree_;
  TFile* outFile_;

  std::vector<std::string> triggerNames_;
  int triggerRes[nMaxTrig];  

  //flags indicating whether the cand passed a certain cms.Path of the analysis
  bool preselM_, finalM_,sbM_;
  bool preselE_, finalE_,sbE_;
  bool preselM1J_, finalM1J_,sbM1J_;
  bool preselE1J_, finalE1J_,sbE1J_;
  bool anyPath_,muPath_,elePath_, singleJetPath_,doubleJetPath_;

  int nCands;
  double hs[nMaxCand], h1[nMaxCand], h2[nMaxCand], phi[nMaxCand], phiS1[nMaxCand], LD[nMaxCand]; // Helicity angles, and LD.
  double mzz[nMaxCand], mll[nMaxCand], mjj[nMaxCand]; // masses
  double ptmzz[nMaxCand];
  double ptlep1[nMaxCand], ptlep2[nMaxCand], etalep1[nMaxCand], etalep2[nMaxCand], philep1[nMaxCand], philep2[nMaxCand];  // lepton kinematics
  double ptjet1[nMaxCand], ptjet2[nMaxCand], etajet1[nMaxCand], etajet2[nMaxCand];
  double phijet1[nMaxCand], phijet2[nMaxCand], massjet1[nMaxCand],massjet2[nMaxCand];  // jet kinematicse
  double  ptmzzNoKinFit[nMaxCand],  mzzNoKinFit[nMaxCand], mjjNoKinFit[nMaxCand],ptjjNoKinFit[nMaxCand],etajjNoKinFit[nMaxCand],phijjNoKinFit[nMaxCand];
  double deltaREDBR[nMaxCand];
  double ptZll[nMaxCand], ptZjj[nMaxCand], yZll[nMaxCand], yZjj[nMaxCand], deltaRleplep[nMaxCand], deltaRjetjet[nMaxCand];
  double phiZll[nMaxCand];//={init};
  double phiZjj[nMaxCand];//={init};
  double met, metSign, metPhi;            // MET and its significance
  double btagjet1[nMaxCand],btagjet2[nMaxCand], lep[nMaxCand], reg[nMaxCand];    // b-tags, lep category, region (sig, sideband)
  double qgjet1[nMaxCand], qgjet2[nMaxCand], qgProduct[nMaxCand];    // QG likelihoods
  double betajet1[nMaxCand],betajet2[nMaxCand],puMvajet1[nMaxCand],puMvajet2[nMaxCand];//jet ID 
  double isolep1[nMaxCand], isolep2[nMaxCand], eleMVAId1[nMaxCand], eleMVAId2[nMaxCand];//lepton ID 
  double isomu1mod[nMaxCand], isomu2mod[nMaxCand]; // modified tracker iso for muons
  double isoele1trk[nMaxCand], isoele2trk[nMaxCand], isoele1calo[nMaxCand], isoele2calo[nMaxCand]; // modified isos for ele
  double HLTSF,PU,PUA,PUB,lumiw,genw,w,wA,wB,vtagw,BTagWeight;          // weight
  double MCmatch[nMaxCand];            // mc matching flag
 
  double qjet[nMaxCand],tau1[nMaxCand],tau2[nMaxCand],nsubj21[nMaxCand],nsubj32[nMaxCand];
// add tau3/4/5 etc.
  double tau3[nMaxCand],tau4[nMaxCand], tau5[nMaxCand];
  double nsubj31[nMaxCand],nsubj41[nMaxCand],nsubj51[nMaxCand],nsubj42[nMaxCand],nsubj52[nMaxCand],nsubj43[nMaxCand],nsubj53[nMaxCand],nsubj54[nMaxCand];
// add fat & sub b jet here for WH
  float nfatjetbtagL[nMaxCand], nfatjetbtagM[nMaxCand], nfatjetbtagT[nMaxCand];
  float nsubjetbtagL[nMaxCand], nsubjetbtagM[nMaxCand], nsubjetbtagT[nMaxCand];
  float dR_subjet[nMaxCand];
  float subjet1_phi[2*nMaxCand],subjet1_eta[2*nMaxCand],subjet2_phi[2*nMaxCand],subjet2_eta[2*nMaxCand];
  int subjet_flavor[2*nMaxCand];

  double mdrop[nMaxCand],prunedmass[nMaxCand];

  int VBFTag[nMaxCand];
  double VBFmJJ[nMaxCand],VBFdeltaEta[nMaxCand],VBFptjet1[nMaxCand],VBFptjet2[nMaxCand],VBFetajet1[nMaxCand],VBFetajet2[nMaxCand],VBFphijet1[nMaxCand],VBFphijet2[nMaxCand];

  double genMassX, genPTX,genYX, genPhiX;
  double genMassZll, genPTZll,genYZll, genPhiZll;
  double genMassZqq, genPTZqq,genYZqq, genPhiZqq;
  double genPTqP,genEtaqP,genPhiqP,genPTqM,genEtaqM, genPhiqM ;
  double genPTlP,genEtalP, genPhilP,genPTlM,genEtalM, genPhilM ;
  double genDRZqq,genDRZll;
  int pdgIdGenX,genFlavqP,genFlavqM,genFlavlP,genFlavlM;



  unsigned int nevent,run,ls, njets, njetspt50, nak5jets , nvtx,npu;
  int q1fl[nMaxCand], q2fl[nMaxCand];
  int nXjets[nMaxCand];//by how many jets is the hadronic V made
  double vTagPurity[nMaxCand];
  //int jjfl[nMaxCand];
  bool readLDFromUserFloat_,  readQGFromUserFloat_;
  HLTConfigProvider hltConfig;

  //flag of the number of loose muons/electrons in one event
  int nLooseMu;
  int nLooseEle;

  //transvers mass of w
  double mt[nMaxCand];

  //number of btagged jets
  double nbtagsL[nMaxCand], nbtagscleanL[nMaxCand];
  double nbtagsM[nMaxCand], nbtagscleanM[nMaxCand];
  double nbtagsT[nMaxCand], nbtagscleanT[nMaxCand];

  //index of events in the cmgtuple, begin from 1
  int nEvt;

  //variables of electron id
  double sigmaIetaIeta[nMaxCand], deltaPhiSuperClusterTrackAtVtx[nMaxCand], deltaEtaSuperClusterTrackAtVtx[nMaxCand], hadronicOverEm[nMaxCand], numberOfHits[nMaxCand], dxy[nMaxCand], dz[nMaxCand], ecalDriven[nMaxCand],convDist[nMaxCand],convDcot[nMaxCand],isConv[nMaxCand], passConversionVeto[nMaxCand];
  double numberOfLostHits[nMaxCand],  e1x5[nMaxCand], e2x5Max[nMaxCand], e5x5[nMaxCand], e1x5Over5x5[nMaxCand], e2x5MaxOver5x5[nMaxCand];
  
  //variables of muon id
  int globalMuon[nMaxCand], nTrackerLayers[nMaxCand], nPixelHits[nMaxCand], nMuonHits[nMaxCand], nMatches[nMaxCand];
  double muondXY[nMaxCand], muondZ[nMaxCand];

  //different type of pz and mWW
  double pz_type0[nMaxCand], pz_type1[nMaxCand], pz_type2[nMaxCand], pz_type3[nMaxCand], pz_type4[nMaxCand];
  double mZZ_type0[nMaxCand],mZZ_type1[nMaxCand],mZZ_type2[nMaxCand],mZZ_type3[nMaxCand],mZZ_type4[nMaxCand];
  double mZZ_type0_ptUncorrected[nMaxCand],mZZ_type1_ptUncorrected[nMaxCand],mZZ_type2_ptUncorrected[nMaxCand],mZZ_type3_ptUncorrected[nMaxCand],mZZ_type4_ptUncorrected[nMaxCand];

  //pt of neutrino before and after the correction
  double pt_neutrino[nMaxCand], pt_neutrino_corrected[nMaxCand];
  double TOBTECjetsId[nMaxCand];
};//end class AnalyzerEDBR 




#endif
