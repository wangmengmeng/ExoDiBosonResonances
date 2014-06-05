#include "ExoDiBosonResonances/EDBRCommon/plugins/AnalyzerEDBR.h"


AnalyzerEDBR::AnalyzerEDBR(const edm::ParameterSet &ps){

  debug_    = ps.getParameter<bool>("debug");
  if(debug_)    cout << "AnalyzerEDBR constructor 555..." << endl;
  isMC_       = ps.getParameter<bool>("isMC");
  treatVBFAsMultiple_    = ps.getParameter<bool>("treatVBFAsMultiple");
  saveVBFCands_   = ps.getParameter<bool>("saveVBFTaggedCands");
  Ngen_     = ps.getParameter<unsigned int>("Ngen");
  xsec_     = ps.getParameter<double>("xsec"); // in fb
  cat_             = ps.getParameter<std::string>("EventCategory");
  XEEColl_         = ps.getParameter<edm::InputTag>("EDBREEJJColl");
  XEELDMap_        = ps.getParameter<edm::InputTag>("EDBREEJJLDValueMap");
  XMMColl_         = ps.getParameter<edm::InputTag>("EDBRMMJJColl");
  XMMLDMap_        = ps.getParameter<edm::InputTag>("EDBRMMJJLDValueMap");
  XEEJColl_        = ps.getParameter<edm::InputTag>("EDBREEJColl");
  XEEJLDMap_       = ps.getParameter<edm::InputTag>("EDBREEJLDValueMap");
  XMMJColl_        = ps.getParameter<edm::InputTag>("EDBRMMJColl");
  XMMJLDMap_       = ps.getParameter<edm::InputTag>("EDBRMMJLDValueMap");
  XQGMap_          = ps.getParameter<edm::InputTag>("EDBRQGValueMap");
// comment and change for WH
//  VType_           = ps.getParameter<std::string>("VType");
  VType1_           = ps.getParameter<std::string>("VType1");
  VType2_           = ps.getParameter<std::string>("VType2");
  fillGen_         = ps.getParameter<unsigned int>("FillGenLevelCode");
  VTagSFHP_          = ps.getParameter<double>("VTaggingScaleFactorHP");
  VTagSFLP_          = ps.getParameter<double>("VTaggingScaleFactorLP");
  //XEENoKinFitLDMap_=ps.getParameter<edm::InputTag>("EDBREENoKinFitLDValueMap");
  //XMMNoKinFitLDMap_=ps.getParameter<edm::InputTag>("EDBRMMNoKinFitLDValueMap");

// comment and change for WH
/*
  if(VType_=="Z"){
    cmgEDBRMu_="cmgEDBRZZMu";
    cmgEDBREle_="cmgEDBRZZEle";
    VpdgId_=23;
    VMass_= 91.1876;
  }
  else if(VType_=="W"){
    cmgEDBRMu_="cmgEDBRWWMu";
    cmgEDBREle_="cmgEDBRWWEle";
    VpdgId_=24;
    VMass_= 80.4;
  } 
  else if(VType_=="H"){
    cmgEDBRMu_="cmgEDBRZZMu";
    cmgEDBREle_="cmgEDBRZZEle";
    VpdgId_=25;
    VMass_= 125;
  }
*/
  if(VType2_=="Z"){
    cmgEDBRMu_="cmgEDBRZZMu";
    cmgEDBREle_="cmgEDBRZZEle";
    VpdgId_=23;
    VMass2_= 91.1876;
  }
  else if(VType2_=="W"){
    cmgEDBRMu_="cmgEDBRWWMu";
    cmgEDBREle_="cmgEDBRWWEle";
    VpdgId_=24;
    VMass2_= 80.4;
  }
  else if(VType2_=="H"){
    cmgEDBRMu_="cmgEDBRWWMu";
    cmgEDBREle_="cmgEDBRWWEle";
    VpdgId_=25;
    VMass2_= 125;
  } 
  else{
// comment and change for WH
//    throw cms::Exception("Wrong parameter")<<"Unrecognized VType paramter: "<<VType_.c_str()<<" . Allowed options are : W ; Z ."<<std::endl;
    throw cms::Exception("Wrong parameter")<<"Unrecognized VType paramter: "<<VType2_.c_str()<<" . Allowed options are :H ."<<std::endl;

  }

  if(XEELDMap_.label()=="" ||XMMLDMap_.label()=="" ) readLDFromUserFloat_=true;
  else readLDFromUserFloat_=false;

  if(XQGMap_.label()=="") readQGFromUserFloat_=true;
  else readQGFromUserFloat_=false;


  outFileName_ = ps.getParameter<string>("outFileName");
  outFile_ = new TFile(outFileName_.c_str(),"recreate");
  if(debug_)cout<<"Storing output TTree in "<<outFileName_.c_str()<<endl;

  triggerNames_ = ps.getParameter< vector<string> >("triggerNames");

  if(cat_!=""){
    if( cat_!="mmjj" &&cat_!="eejj" && cat_!="mmj" && cat_!="eej"){
      throw cms::Exception("AnalyzerEDBR: Wrong event category passed as input. Possibilities are: mmjj, eejj, mmj, eej");
    }
  }

  if(debug_)cout<<"Initializing"<<endl;

  init();
  if(debug_)cout<<"Initialization is over"<<endl;

}//end constructor


void AnalyzerEDBR::analyze(edm::Event const& iEvent, edm::EventSetup const& eventSetup){

  //use these for X->ZZ analysis
 /* 
  typedef  cmg::DiElectronSingleJetEDBR cmgEleSingleJetEDBR ;
  typedef  cmg::DiMuonSingleJetEDBR     cmgMuSingleJetEDBR  ;
  typedef  cmg::DiElectronDiJetEDBR     cmgEleDiJetEDBR  ;
  typedef  cmg::DiMuonDiJetEDBR         cmgMuDiJetEDBR  ;
  */
// comment and change for WH
/*
  //use these for X->WW analysis
   
      typedef  cmg::WelenuSingleJetEDBR cmgEleSingleJetEDBR ;
      typedef  cmg::WmunuSingleJetEDBR  cmgMuSingleJetEDBR  ; 
      typedef  cmg::WelenuDiJetEDBR     cmgEleDiJetEDBR  ;
      typedef  cmg::WmunuDiJetEDBR      cmgMuDiJetEDBR  ;
*/ 
// use these for X->WH analysis
      typedef  cmg::WelenuSingleJetEDBR cmgEleSingleJetEDBR ;
      typedef  cmg::WmunuSingleJetEDBR  cmgMuSingleJetEDBR  ;
      typedef  cmg::WelenuDiJetEDBR     cmgEleDiJetEDBR  ;
      typedef  cmg::WmunuDiJetEDBR      cmgMuDiJetEDBR  ;  

  nEvt++;

  if(debug_) cout<<"\n\nAnalyzing event"<<endl;
  initDataMembers();

  nevent = iEvent.eventAuxiliary().event();
  run    = iEvent.eventAuxiliary().run();
  ls     = iEvent.eventAuxiliary().luminosityBlock();
  if(debug_) cout<<endl<<" Run "<<run<<"  Event "<<nevent<<endl;


  // GET VERTICES
  edm::Handle<reco::VertexCollection> vertexCollection;
  if(iEvent.getByLabel("offlinePrimaryVertices",vertexCollection))  nvtx=vertexCollection->size();
  else{
    if(debug_)cout<<"WARNING: VertexCollection called \'offlinePrimaryVertices\' NOT FOUND !"<<endl;
    nvtx=0;
  }
  npu=-1;

  //total number of pre-selected jets in the event
  edm::Handle<std::vector<cmg::PFJet> > allJets;
  iEvent.getByLabel("jetIDJet", allJets);
  //cout<<allJets->size()<<endl;
  std::vector<cmg::PFJet>::const_iterator idjet;
  njetspt50=0;
  //make cut on "jetIDJet", requiring pt>50 GeV, and then count the number
  for(idjet = allJets->begin(); idjet != allJets->end(); ++idjet ){
    if(idjet->pt()>50)njetspt50++;
  }
  njets=allJets->size();
  //cout<<njets<<endl;

  //total number of AK5 jets (cleaned) used for btagging
  //edm::Handle<std::vector<cmg::PFJet> > ak5jets;
  //iEvent.getByLabel("jetAK5", ak5jets);
  //nak5jets=ak5jets->size();

  // GET MISSING ET
  edm::Handle<edm::View<pat::MET> > metHandle;
// comment and change for WH
//  if(VType_=="Z")iEvent.getByLabel("patMETs", metHandle);
//  else if(VType_=="W")iEvent.getByLabel("patMetShiftCorrected", metHandle);
  if(VType1_=="Z")iEvent.getByLabel("patMETs", metHandle);
  else if(VType1_=="W")iEvent.getByLabel("patMetShiftCorrected", metHandle);
  met     = metHandle->at(0).pt();
  metSign = metHandle->at(0).significance(); 
  metPhi  = metHandle->at(0).phi();

  analyzeTrigger(iEvent, eventSetup);

  ///  bool eleEvent   = elePath_; //&&(cat_=="eejj" || cat_=="eej")
  ///  bool muEvent    = muPath_;
  bool goodKinFit = true;
  bool singleJetEvent=false;
  bool doubleJetEvent=false;

  if(isMC_) analyzeGenLevel(iEvent, eventSetup);


  // edm::Handle<edm::ValueMap<float> > qgmap;
  // if(anyPath_){
  //  if(!readQGFromUserFloat_)iEvent.getByLabel(HiggsQGMap_, qgmap);
  // }


  //edm::Handle<std::vector< cmg::DiPFJet > >   dijets;
  //  edm::Handle<std::vector< cmg::DiObject<cmg::PFJet,cmg::PFJet> > >   dijetskinfit;
  // edm::Handle<std::vector< cmg::DiObject<cmg::PFJet,cmg::PFJet> > >  zjjs;
  //if( iEvent.getByLabel(  "cmgDiJet"  , dijets  ) && iEvent.getByLabel(  "cmgDiJetKinFit"  , dijetskinfit  ) && iEvent.getByLabel(  "ZjjCand"  , zjjs  ) ){                 
  // cout<<"Size of Dijet Collections---> cmgDiJet: "<<dijets->size()<<"   cmgDijetKinFit: "<<dijetskinfit->size()<<"  Zjj: "<<zjjs->size()<<endl;
  // }

  if(muPath_){


    if(singleJetPath_){

      edm::Handle<edm::View< cmgMuSingleJetEDBR > > finalEDBRcand;
      iEvent.getByLabel(XMMJColl_        , finalEDBRcand  );  // With kinfit


      int nCollCandidates=finalEDBRcand->size();
      if ( nCollCandidates+nCands > nMaxCand ) nCollCandidates = nMaxCand - nCands;
      if(debug_)cout<<"read from MUON event, there are "<<nCollCandidates<<" X->ZZ->2L1J cands"<<endl;
      int ih = nCands;
      bool vbfFound=false;
      for(int icand=0;icand<nCollCandidates;icand++){

	edm::RefToBase<cmgMuSingleJetEDBR> edbrM =finalEDBRcand->refAt(icand);

	//	  if(edbrM->nJets()!=1){
	//throw cms::Exception("Mismatched param") <<"Event in SingleJet Path has "<<edbrM->nJets()
	//				     <<" jets"<<std::endl;  
	//}

	bool keepThisVBFCand=true;
	int vbfTest=checkVBFTag(edbrM,ih,vbfFound,keepThisVBFCand);
	if(vbfTest>0)vbfFound=true;	  
	if(vbfTest>0 && !saveVBFCands_)continue; //skip all vbf-tagged cands	 	 
	if(vbfTest>0 &&!keepThisVBFCand) continue; 

	VBFTag[ih] = vbfTest;

	analyzeGeneric(edbrM, ih);
	analyzeSingleJet(edbrM,ih);        
	analyzeMuon(edbrM,ih);
	analyzeVBF(edbrM,ih, vbfTest);
// comment and change for WH
//	if(VType_=="W")CalculateMWW(edbrM,ih,1);
        if(VType2_=="H")CalculateMWW(edbrM,ih,1);

	ih++;
      }//end loop on candidates
      // if(debug_)cout<<"Adding "<<ih<<" muCands"<<endl;
      nCands = ih;
      singleJetEvent=true;
    }//end if singleJetPath

    if(doubleJetPath_){
      edm::Handle<edm::View< cmgMuDiJetEDBR > > finalEDBRcand;
      iEvent.getByLabel(XMMColl_        , finalEDBRcand  );  // With kinfit


      int nCollCandidates=finalEDBRcand->size();

      if (nCollCandidates+nCands> nMaxCand) nCollCandidates = nMaxCand-nCands;

      if(debug_)cout<<"read from MUON event, there are "<<nCollCandidates<<" X->ZZ->2L2J cands"<<endl;
      int ih = nCands;
      bool vbfFound=false;
      for(int icand=0;icand<nCollCandidates;icand++){

	edm::RefToBase<cmgMuDiJetEDBR> edbrM =finalEDBRcand->refAt(icand);


	//  if(edbrM->nJets()!=2){
	//  throw cms::Exception("Mismatched param") <<"Event in DoubleJet Path has "<<edbrM->nJets()
	//						     <<" jets"<<std::endl;  
	// }

	bool keepThisVBFCand=true;
	int vbfTest=checkVBFTag(edbrM,ih,vbfFound,keepThisVBFCand);
	if(vbfTest>0)vbfFound=true;	  
	if(vbfTest>0 && !saveVBFCands_)continue; //skip all vbf-tagged cands	 	 
	if(vbfTest>0 &&!keepThisVBFCand) continue; 

	VBFTag[ih] = vbfTest;

	analyzeGeneric(edbrM,ih);
	analyzeDoubleJet(edbrM,ih,goodKinFit);        
	analyzeMuon(edbrM,ih);
	analyzeVBF(edbrM,ih, vbfTest);
// comment and change for WH
//	if(VType_=="W")CalculateMWW(edbrM,ih,1);
        if(VType2_=="H")CalculateMWW(edbrM,ih,1);

	ih++;
      }//end loop on candidates

      nCands = ih;
      doubleJetEvent=true;
    }//end if doubleJetPath

  }//end if mmjj


  //  if(cat_=="eejj"){
  if(elePath_){


    if(singleJetPath_){
      edm::Handle<edm::View< cmgEleSingleJetEDBR > > finalEDBRcand;
      iEvent.getByLabel(XEEJColl_        , finalEDBRcand  );  // With kinfit


      int nCollCandidates=finalEDBRcand->size();
      if (nCollCandidates+nCands > nMaxCand) nCollCandidates = nMaxCand-nCands;
      if(debug_)cout<<"read from ELECTRON event, there are "<<nCollCandidates<<" X->ZZ->2L1J cands"<<endl;
      int ih = nCands;
      bool vbfFound=false;
      for(int icand=0;icand<nCollCandidates;icand++){

	edm::RefToBase< cmgEleSingleJetEDBR > edbrE =finalEDBRcand->refAt(icand);

	//  if(edbrE->nJets()!=1){
	//  throw cms::Exception("Mismatched param") <<"Event in SingleJet Path has "<<edbrE->nJets()
	//						     <<" jets"<<std::endl;  
	// }

	bool keepThisVBFCand=true;
	int vbfTest=checkVBFTag(edbrE,ih,vbfFound,keepThisVBFCand);
	if(vbfTest>0)vbfFound=true;	  
	if(vbfTest>0 && !saveVBFCands_)continue; //skip all vbf-tagged cands	 	 
	if(vbfTest>0 &&!keepThisVBFCand) continue; 

	VBFTag[ih] = vbfTest;

	analyzeGeneric(edbrE, ih);
	analyzeSingleJet(edbrE,ih);        
	analyzeElectron(edbrE,ih);
	analyzeVBF(edbrE,ih, vbfTest);
// comment and change for WH
//	if(VType_=="W")CalculateMWW(edbrE,ih,0);
        if(VType2_=="H")CalculateMWW(edbrE,ih,0);

	ih++;
      }//end loop on candidates
      // if(debug_)cout<<"Adding "<<ih<<" muCands"<<endl;
      nCands = ih;

    }//end if singleJetPath



    if(doubleJetPath_){
      edm::Handle<edm::View< cmgEleDiJetEDBR > > finalEDBRcand;
      iEvent.getByLabel(XEEColl_        , finalEDBRcand  );  // With kinfit

      int nCollCandidates=finalEDBRcand->size();
      if (nCollCandidates+nCands > nMaxCand) nCollCandidates = nMaxCand-nCands;

      if(debug_){
	cout<<"read from ELECTRON event, there are "<<nCollCandidates<<" X->ZZ->2L2J cands"<<endl;


	for(int icand=0;icand<nCollCandidates;icand++){
	  cout<<"Loop on ELE cand ih="<<icand<<"  Mass="<<finalEDBRcand->refAt(icand)->mass() <<" Mll="<<finalEDBRcand->refAt(icand)->leg1().mass() <<" Mjj="<<finalEDBRcand->refAt(icand)->leg2().mass() <<" Etajj="<<finalEDBRcand->refAt(icand)->leg2().eta()<<std::flush;
	  if(finalEDBRcand->refAt(icand)->vbfptr().isAvailable())cout<<" Mass_vbf="<<finalEDBRcand->refAt(icand)->vbfptr()->mass()<<std::endl;
	  else cout<<" Mass_vbf= n.a."<<std::endl;
	}


      }//end if debug

      int ih = nCands;
      bool vbfFound=false;
      for(int icand=0;icand<nCollCandidates;icand++){
	//  cout<<"Loop on ELE cand ih="<<icand<<std::flush;
	edm::RefToBase<cmgEleDiJetEDBR> edbrE =finalEDBRcand->refAt(icand);


	// if(edbrE->nJets()!=2){
	//  throw cms::Exception("Mismatched param") <<"Event in DoubleJet Path has "<<edbrE->nJets()
	//						     <<" jets"<<std::endl;  
	// }

	bool keepThisVBFCand=true;
	int vbfTest=checkVBFTag(edbrE,ih,vbfFound,keepThisVBFCand);
	if(vbfTest>0)vbfFound=true;	  
	if(vbfTest>0 && !saveVBFCands_)continue; //skip all vbf-tagged cands	 	 
	if(vbfTest>0 &&!keepThisVBFCand) continue; 

	VBFTag[ih] = vbfTest;

	analyzeGeneric(edbrE,ih);
	analyzeDoubleJet(edbrE, ih,goodKinFit);        
	analyzeElectron(edbrE,ih);
	analyzeVBF(edbrE,ih, vbfTest);
// comment and change for WH
//	if(VType_=="W")CalculateMWW(edbrE,ih,0);
        if(VType2_=="H")CalculateMWW(edbrE,ih,0);

	ih++;
      }//end loop on candidates
      // if(debug_)cout<<"Adding "<<ih<<" muCands"<<endl;
      nCands = ih;
    }//end if doubleJetPath
  }//end if electron channel


  //EVENT WEIGHTS
  if(isMC_){
    // Ngen=Ngen_;
    lumiw = xsec_/Ngen_;
    edm::Handle<GenEventInfoProduct> hGenEvtInfo;
    if(iEvent.getByLabel("generator",hGenEvtInfo)){
      genw=hGenEvtInfo->weights()[0];
    }

    //apply V-tagging scale factor from specific ttbar studies
    //vtagw=VTagSF_;
  }
  if(debug_)  cout<<"lumi weight="<<lumiw<<"  PU weight="<<PU<<endl;
  w  = PU *HLTSF*genw*lumiw*vtagw*BTagWeight;
  wA = PUA*HLTSF*genw*lumiw*vtagw*BTagWeight;
  wB = PUB*HLTSF*genw*lumiw*vtagw*BTagWeight;


  bool passCuts=true;
  bool storeEvt=goodKinFit && (muPath_ || elePath_)  && passCuts;
  //  if(debug_&& singleJetEvent&&doubleJetEvent)cout<<" Run "<<run<<"  Event "<<nevent<<"\tThis muon-event has both single and double jet topology."<<endl;
  if( singleJetEvent&&doubleJetEvent &&debug_)cout<<" Run "<<run<<"  Event "<<nevent<<"\tThis muon-event has both single and double jet topology."<<endl;
  if(storeEvt){
    //  if(debug_)cout<<"Filling the tree ("<<nCands<<endl;//" cands -> pTlep1="<< ptlep1[nCands-1]<<")"<<endl;
    outTree_->Fill(); 
    //  if(debug_)cout<<" filled."<<endl;
  }

  /// &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

  if(debug_)cout<<"Finished AnalyzerEDBR::analyze for Run "<<run<<"  Event "<<nevent<<endl;
}//
//end AnalyzerEDBR::analyze



void AnalyzerEDBR::init(){

  initTree();
  nEvt=0;



}//end init()


void AnalyzerEDBR::initTree(){

  if(debug_)cout<<"creating the output TTree"<<endl;
  outTree_ = new TTree("SelectedCandidates","angles etc.");
  outTree_->Branch("nEvt"            ,&nEvt          ,"nEvt/I"                 );
  outTree_->Branch("nCands"          ,&nCands        ,"nCands/I"               );
  outTree_->Branch("event"           ,&nevent        ,"event/i"                );
  outTree_->Branch("run"             ,&run           ,"run/i"                  );
  outTree_->Branch("ls"              ,&ls            ,"ls/i"                   );
  outTree_->Branch("cosThetaStar"    ,&hs            ,"cosThetaStar[nCands]/D" );
  outTree_->Branch("cosTheta1"       ,&h1            ,"cosTheta1[nCands]/D"    );
  outTree_->Branch("cosTheta2"       ,&h2            ,"cosTheta2[nCands]/D"    );
  outTree_->Branch("phi"             ,&phi           ,"phi[nCands]/D"          );
  outTree_->Branch("phiStar1"        ,&phiS1         ,"phiStar1[nCands]/D"     );
  outTree_->Branch("ptlep1"          ,&ptlep1        ,"ptlep1[nCands]/D"       );
  outTree_->Branch("ptlep2"          ,&ptlep2        ,"ptlep2[nCands]/D"       );
  outTree_->Branch("ptjet1"          ,&ptjet1        ,"ptjet1[nCands]/D"       );
  outTree_->Branch("ptjet2"          ,&ptjet2        ,"ptjet2[nCands]/D"       );
  outTree_->Branch("ptZll"           ,&ptZll         ,"ptZll[nCands]/D"        );
  outTree_->Branch("ptZjj"           ,&ptZjj         ,"ptZjj[nCands]/D"        );
  outTree_->Branch("yZll"            ,&yZll          ,"yZll[nCands]/D"         );
  outTree_->Branch("yZjj"            ,&yZjj          ,"yZjj[nCands]/D"         );
  outTree_->Branch("phiZll"          ,&phiZll        ,"phiZll[nCands]/D"       );
  outTree_->Branch("phiZjj"          ,&phiZjj        ,"phiZjj[nCands]/D"       );
  outTree_->Branch("etalep1"         ,&etalep1       ,"etalep1[nCands]/D"      );
  outTree_->Branch("etalep2"         ,&etalep2       ,"etalep2[nCands]/D"      );
  outTree_->Branch("etajet1"         ,&etajet1       ,"etajet1[nCands]/D"      );
  outTree_->Branch("etajet2"         ,&etajet2       ,"etajet2[nCands]/D"      );
  outTree_->Branch("philep1"         ,&philep1       ,"philep1[nCands]/D"      );
  outTree_->Branch("philep2"         ,&philep2       ,"philep2[nCands]/D"      );
  outTree_->Branch("phijet1"         ,&phijet1       ,"phijet1[nCands]/D"      );
  outTree_->Branch("phijet2"         ,&phijet2       ,"phijet2[nCands]/D"      );
  outTree_->Branch("massjet1"         ,&massjet1       ,"massjet1[nCands]/D"      );
  outTree_->Branch("massjet2"         ,&massjet2       ,"massjet2[nCands]/D"      );
  outTree_->Branch("lep"             ,&lep           ,"lep[nCands]/D"          );
  outTree_->Branch("mt"              ,&mt            ,"mt[nCands]/D"           );
  outTree_->Branch("region"          ,&reg           ,"region[nCands]/D"       );
  outTree_->Branch("nXjets"          ,&nXjets        ,"nXjets[nCands]/I"    ); 
  outTree_->Branch("vTagPurity"      ,&vTagPurity    ,"vTagPurity[nCands]/D"    ); 
  outTree_->Branch("mZZ"             ,&mzz           ,"mZZ[nCands]/D"          );
  outTree_->Branch("mZZNoKinFit"     ,&mzzNoKinFit   ,"mZZNoKinFit[nCands]/D"  );
  outTree_->Branch("ptmzz"           ,&ptmzz         ,"ptmzz[nCands]/D"        );
  outTree_->Branch("ptmzzNoKinFit"   ,&ptmzzNoKinFit ,"ptmzzNoKinFit[nCands]/D");
  outTree_->Branch("mLL"             ,&mll           ,"mLL[nCands]/D"          );
  outTree_->Branch("mJJ"             ,&mjj           ,"mJJ[nCands]/D"          );
  outTree_->Branch("mJJNoKinFit"     ,&mjjNoKinFit   ,"mJJNoKinFit[nCands]/D"  );
  outTree_->Branch("met"             ,&met           ,"met/D"                  );
  outTree_->Branch("metSign"         ,&metSign       ,"metSign/D"              );
  outTree_->Branch("metPhi"         ,&metPhi       ,"metPhi/D"              );
  //outTree_->Branch("nBTags"          ,&btag          ,"nBTags[nCands]/D"       );
  outTree_->Branch("btagjet1"         ,&btagjet1       ,"btagjet1/D"              );
  outTree_->Branch("btagjet2"         ,&btagjet2       ,"btagjet2/D"              );
  outTree_->Branch("deltaREDBR"     ,&deltaREDBR   ,"deltaREDBR[nCands]/D"  );
  outTree_->Branch("deltaRleplep"    ,&deltaRleplep  ,"deltaRleplep[nCands]/D" );
  outTree_->Branch("deltaRjetjet"    ,&deltaRjetjet  ,"deltaRjetjet[nCands]/D" );
  outTree_->Branch("qgProduct"       ,&qgProduct     ,"qgProduct[nCands]/D"    );
  outTree_->Branch("qgjet1"          ,&qgjet1        ,"qgjet1[nCands]/D"       );
  outTree_->Branch("qgjet2"          ,&qgjet2        ,"qgjet2[nCands]/D"       );
  outTree_->Branch("betajet1"        ,&betajet1      ,"betajet1[nCands]/D"     ); 
  outTree_->Branch("betajet2"        ,&betajet2      ,"betajet2[nCands]/D"     ); 
  outTree_->Branch("puMvajet1"       ,&puMvajet1     ,"puMvajet1[nCands]/D"    ); 
  outTree_->Branch("puMvajet2"       ,&puMvajet2     ,"puMvajet2[nCands]/D"    ); 
  outTree_->Branch("prunedmass"       ,&prunedmass    ,"prunedmass[nCands]/D"    ); 
  outTree_->Branch("mdrop"       ,&mdrop     ,"mdrop[nCands]/D"    ); 
  outTree_->Branch("nsubj21"       ,&nsubj21    ,"nsubj21[nCands]/D"    ); 
  outTree_->Branch("nsubj32"       ,&nsubj32     ,"nsubj32[nCands]/D"    ); 
  outTree_->Branch("tau1"       ,&tau1     ,"tau1[nCands]/D"    ); 
  outTree_->Branch("tau2"       ,&tau2    ,"tau2[nCands]/D"    ); 
// add tau3/4/5 etc.
  outTree_->Branch("tau3"       ,&tau3    ,"tau3[nCands]/D"    );
  outTree_->Branch("tau4"       ,&tau4    ,"tau4[nCands]/D"    );
  outTree_->Branch("tau5"       ,&tau5    ,"tau5[nCands]/D"    );
  outTree_->Branch("nsubj31"       ,&nsubj31    ,"nsubj31[nCands]/D"    );
  outTree_->Branch("nsubj41"       ,&nsubj41     ,"nsubj41[nCands]/D"    );
  outTree_->Branch("nsubj51"       ,&nsubj51    ,"nsubj51[nCands]/D"    );
  outTree_->Branch("nsubj42"       ,&nsubj42     ,"nsubj42[nCands]/D"    );
  outTree_->Branch("nsubj52"       ,&nsubj52    ,"nsubj52[nCands]/D"    );
  outTree_->Branch("nsubj43"       ,&nsubj43     ,"nsubj43[nCands]/D"    );
  outTree_->Branch("nsubj53"       ,&nsubj53    ,"nsubj53[nCands]/D"    );
  outTree_->Branch("nsubj54"       ,&nsubj54     ,"nsubj54[nCands]/D"    );
// add fat & sub b jet here for WH
  outTree_->Branch("nfatjetbtagL"      ,&nfatjetbtagL   ,"nfatjetbtagL[nCands]/F"   );
  outTree_->Branch("nfatjetbtagM"      ,&nfatjetbtagM   ,"nfatjetbtagM[nCands]/F"   );
  outTree_->Branch("nfatjetbtagT"      ,&nfatjetbtagT   ,"nfatjetbtagT[nCands]/F"   );

  outTree_->Branch("nsubjetbtagL"      ,&nsubjetbtagL   ,"nsubjetbtagL[nCands]/F"   );
  outTree_->Branch("nsubjetbtagM"      ,&nsubjetbtagM   ,"nsubjetbtagM[nCands]/F"   );
  outTree_->Branch("nsubjetbtagT"      ,&nsubjetbtagT   ,"nsubjetbtagT[nCands]/F"   );

  outTree_->Branch("subjet_flavor"      ,&subjet_flavor   ,"subjet_flavor[nCands]/I"   );
  outTree_->Branch("dR_subjet"      ,&dR_subjet   ,"dR_subjet[nCands]/F"   );
  outTree_->Branch("subjet1_phi"    ,&subjet1_phi, "subjet1_phi[nCands]/F");
  outTree_->Branch("subjet1_eta"    ,&subjet1_eta, "subjet1_eta[nCands]/F");
  outTree_->Branch("subjet2_phi"    ,&subjet2_phi, "subjet2_phi[nCands]/F");
  outTree_->Branch("subjet2_eta"    ,&subjet2_eta, "subjet2_eta[nCands]/F");

  outTree_->Branch("qjet"       ,&qjet    ,"qjet[nCands]/D"    ); 
  outTree_->Branch("isolep1"         ,&isolep1       ,"isolep1[nCands]/D"      ); 
  outTree_->Branch("isolep2"         ,&isolep2       ,"isolep2[nCands]/D"      ); 
  outTree_->Branch("isomu1mod"         ,&isomu1mod       ,"isomu1mod[nCands]/D"      ); 
  outTree_->Branch("isomu2mod"         ,&isomu2mod       ,"isomu2mod[nCands]/D"      ); 
  outTree_->Branch("isoele1trk"        ,&isoele1trk      ,"isoele1trk[nCands]/D"      ); 
  outTree_->Branch("isoele2trk"        ,&isoele2trk      ,"isoele2trk[nCands]/D"      ); 
  outTree_->Branch("isoele1calo"       ,&isoele1calo     ,"isoele1calo[nCands]/D"      ); 
  outTree_->Branch("isoele2calo"       ,&isoele2calo     ,"isoele2calo[nCands]/D"      ); 
  outTree_->Branch("eleMVAId1"       ,&eleMVAId1     ,"eleMVAId1[nCands]/D"    );
  outTree_->Branch("eleMVAId2"       ,&eleMVAId2     ,"eleMVAId2[nCands]/D"    );
  outTree_->Branch("LD"              ,&LD            ,"LD[nCands]/D"           );
  //outTree_->Branch("aplanarity"      ,&aplanarity    ,"aplanarity[nCands]/D"   );
  // outTree_->Branch("sphericity"      ,&sphericity    ,"sphericity[nCands]/D"   );
  // outTree_->Branch("centrality"      ,&centrality    ,"centrality[nCands]/D"   );
  outTree_->Branch("q1fl"            ,&q1fl          ,"q1fl[nCands]/I"         );
  outTree_->Branch("q2fl"            ,&q2fl          ,"q2fl[nCands]/I"         );
  //outTree_->Branch("jjfl"            ,&jjfl          ,"jjfl[nCands]/I"         );
  outTree_->Branch("MCmatch"         ,&MCmatch       ,"MCmatch[nCands]/D"      );
  outTree_->Branch("nVtx"            ,&nvtx          ,"nVtx/i"                 );
  outTree_->Branch("nJets"           ,&njets         ,"nJets/i"                );
  outTree_->Branch("nJetsPt50"       ,&njetspt50     ,"nJetsPt50/i"                );
  outTree_->Branch("nAK5jets"        ,&nak5jets      ,"nAK5jets/i"             );
  outTree_->Branch("nPU"             ,&npu           ,"nPU/i"                  );
  outTree_->Branch("HLTweight"       ,&HLTSF         ,"HLTweight/D"            ); 
  outTree_->Branch("BTagWeight"      ,&BTagWeight    ,"BTagWeight/D"           ); 
  outTree_->Branch("PUweight"        ,&PU            ,"PUweight/D"             ); 
  outTree_->Branch("PUweight2012A"   ,&PUA           ,"PUweight2012A/D"        ); 
  outTree_->Branch("PUweight2012B"   ,&PUB           ,"PUweight2012B/D"        );
  outTree_->Branch("LumiWeight"      ,&lumiw          ,"LumiWeight/D"           );  // For correct lumi scaling
  outTree_->Branch("GenWeight"       ,&genw          ,"GenWeight/D"            );  // Gen level MC weights
  outTree_->Branch("VTagWeight"      ,&vtagw          ,"VTagWeight/D"            );  //Vtagging scale factor
  outTree_->Branch("weight"          ,&w             ,"weight/D"               );  // Product of PU and lumi weights
  outTree_->Branch("weight2012A"     ,&wA            ,"weight2012A/D"          );
  outTree_->Branch("weight2012B"     ,&wB            ,"weight2012B/D"          );
  outTree_->Branch("VBFTag"          ,&VBFTag     ,"VBFTag[nCands]/I"    ); 
  outTree_->Branch("VBFmJJ"          ,&VBFmJJ     ,"VBFmJJ[nCands]/D"    ); 
  outTree_->Branch("VBFdeltaEta"     ,&VBFdeltaEta     ,"VBFdeltaEta[nCands]/D"    ); 
  outTree_->Branch("VBFptjet1"       ,&VBFptjet1     ,"VBFptjet1[nCands]/D"    ); 
  outTree_->Branch("VBFptjet2"       ,&VBFptjet2     ,"VBFptjet2[nCands]/D"    ); 
  outTree_->Branch("VBFetajet1"       ,&VBFetajet1     ,"VBFetajet1[nCands]/D"    ); 
  outTree_->Branch("VBFetajet2"       ,&VBFetajet2     ,"VBFetajet2[nCands]/D"    ); 
  outTree_->Branch("VBFphijet1"       ,&VBFphijet1     ,"VBFphijet1[nCands]/D"    ); 
  outTree_->Branch("VBFphijet2"       ,&VBFphijet2     ,"VBFphijet2[nCands]/D"    ); 
  outTree_->Branch("genMass_X"        ,&genMassX      ,"genMass_X/d"             );
  outTree_->Branch("genPT_X"          ,&genPTX        ,"genPT_X/d"               );
  outTree_->Branch("genY_X"           ,&genYX         ,"genY_X/d"                );
  outTree_->Branch("genPhi_X"         ,&genPhiX       ,"genPhi_X/d"              );
  outTree_->Branch("genPdgId_X"       ,&pdgIdGenX     ,"genPdgId_X/I"            );
  outTree_->Branch("genMass_Vll"      ,&genMassZll    ,"genMass_Vll/d"           );
  outTree_->Branch("genPT_Vll"        ,&genPTZll      ,"genPT_Vll/d"             );
  outTree_->Branch("genY_Vll"         ,&genYZll       ,"genY_Vll/d"              );
  outTree_->Branch("genPhi_Vll"       ,&genPhiZll     ,"genPhi_Vll/d"            );
  outTree_->Branch("genDeltaRll_Vll"  ,&genDRZll     ,"genDeltaRll_Vll/d"   );
  outTree_->Branch("genMass_Vqq"      ,&genMassZqq    ,"genMass_Vqq/d"           );
  outTree_->Branch("genPT_Vqq"        ,&genPTZqq      ,"genPT_Vqq/d"             );
  outTree_->Branch("genY_Vqq"         ,&genYZqq       ,"genY_Vqq/d"              );
  outTree_->Branch("genPhi_Vqq"       ,&genPhiZqq     ,"genPhi_Vqq/d"            );
  outTree_->Branch("genDeltaRqq_Vqq"       ,&genDRZqq     ,"genDeltaRqq_Vqq/d"   );
  //
  outTree_->Branch("genPT_qP"         ,&genPTqP       ,"genPT_qP/d"           );
  outTree_->Branch("genEta_qP"        ,&genEtaqP      ,"genEta_qP/d"             );
  outTree_->Branch("genPhi_qP"        ,&genPhiqP      ,"genPhi_qP/d"              );
  outTree_->Branch("genFlav_qP"       ,&genFlavqP     ,"genFlav_qP/I"              );
  outTree_->Branch("genPT_qM"         ,&genPTqM       ,"genPT_qM/d"           );
  outTree_->Branch("genEta_qM"        ,&genEtaqM      ,"genEta_qM/d"             );
  outTree_->Branch("genPhi_qM"        ,&genPhiqM      ,"genPhi_qM/d"              );
  outTree_->Branch("genFlav_qM"       ,&genFlavqM     ,"genFlav_qM/I"              );
  outTree_->Branch("genPT_lP"         ,&genPTlP       ,"genPT_lP/d"           );
  outTree_->Branch("genEta_lP"        ,&genEtalP      ,"genEta_lP/d"             );
  outTree_->Branch("genPhi_lP"        ,&genPhilP      ,"genPhi_lP/d"              );
  outTree_->Branch("genFlav_lP"       ,&genFlavlP     ,"genFlav_lP/I"              );
  outTree_->Branch("genPT_lM"         ,&genPTlM       ,"genPT_lM/d"           );
  outTree_->Branch("genEta_lM"        ,&genEtalM      ,"genEta_lM/d"          );
  outTree_->Branch("genPhi_lM"        ,&genPhilM      ,"genPhi_lM/d"          );
  outTree_->Branch("genFlav_lM"       ,&genFlavlM     ,"genFlav_lM/I"         );
  //
  outTree_->Branch("nLooseMu"        ,&nLooseMu      ,"nLooseMu/I"             );
  outTree_->Branch("nLooseEle"       ,&nLooseEle     ,"nLooseEle/I"            );
  outTree_->Branch("nbtagsL"          ,&nbtagsL        ,"nbtagsL[nCands]/D"       );
  outTree_->Branch("nbtagsM"          ,&nbtagsM        ,"nbtagsM[nCands]/D"       );
  outTree_->Branch("nbtagsT"          ,&nbtagsT        ,"nbtagsT[nCands]/D"       );
  outTree_->Branch("nbtagscleanL"     ,&nbtagscleanL   ,"nbtagscleanL[nCands]/D"  );
  outTree_->Branch("nbtagscleanM"     ,&nbtagscleanM   ,"nbtagscleanM[nCands]/D"  );
  outTree_->Branch("nbtagscleanT"     ,&nbtagscleanT   ,"nbtagscleanT[nCands]/D"  );
  outTree_->Branch("eleid_sigmaIetaIeta"     ,&sigmaIetaIeta   ,"eleid_sigmaIetaIeta[nCands]/D"  );
  outTree_->Branch("eleid_deltaPhiSuperClusterTrackAtVtx"     ,&deltaPhiSuperClusterTrackAtVtx   ,"eleid_deltaPhiSuperClusterTrackAtVtx[nCands]/D"  );
  outTree_->Branch("eleid_deltaEtaSuperClusterTrackAtVtx"     ,&deltaEtaSuperClusterTrackAtVtx   ,"eleid_deltaEtaSuperClusterTrackAtVtx[nCands]/D"  );
  outTree_->Branch("eleid_hadronicOverEm"     ,&hadronicOverEm   ,"eleid_hadronicOverEm[nCands]/D"  );
  outTree_->Branch("eleid_numberOfHits"     ,&numberOfHits   ,"eleid_numberOfHits[nCands]/D"  );
  outTree_->Branch("eleid_dxy"     ,&dxy   ,"eleid_dxy[nCands]/D"  );
  outTree_->Branch("eleid_dz"     ,&dz   ,"eleid_dz[nCands]/D"  );
  outTree_->Branch("eleid_ecalDriven"     ,&ecalDriven   ,"eleid_ecalDriven[nCands]/D"  );	
  outTree_->Branch("eleid_convDist"     ,&convDist   ,"eleid_convDist[nCands]/D"  );	
  outTree_->Branch("eleid_convDcot"     ,&convDcot   ,"eleid_convDcot[nCands]/D"  );	
  outTree_->Branch("eleid_isConv"     ,&isConv   ,"eleid_isConv[nCands]/D"  );
  outTree_->Branch("eleid_passConversionVeto"     ,&passConversionVeto   ,"eleid_passConversionVeto[nCands]/D"  );
  outTree_->Branch("eleid_numberOfLostHits"     ,&numberOfLostHits   ,"eleid_numberOfLostHits[nCands]/D"  );
  outTree_->Branch("eleid_e1x5"     ,&e1x5   ,"eleid_e1x5[nCands]/D"  );
  outTree_->Branch("eleid_e2x5Max"     ,&e2x5Max   ,"eleid_e2x5Max[nCands]/D"  );
  outTree_->Branch("eleid_e5x5"     ,&e5x5   ,"eleid_e5x5[nCands]/D"  );
  outTree_->Branch("eleid_e1x5Over5x5"     ,&e1x5Over5x5   ,"eleid_e1x5Over5x5[nCands]/D"  );
  outTree_->Branch("eleid_e2x5MaxOver5x5"     ,&e2x5MaxOver5x5   ,"eleid_e2x5MaxOver5x5[nCands]/D"  );

  outTree_->Branch("muonid_globalMuon", &globalMuon, "muonid_globalMuon[nCands]/I");
  outTree_->Branch("muonid_nTrackerLayers", &nTrackerLayers, "muonid_nTrackerLayers[nCands]/I");
  outTree_->Branch("muonid_nPixelHits", &nPixelHits, "muonid_nPixelHits[nCands]/I");
  outTree_->Branch("muonid_nMuonHits", &nMuonHits, "muonid_nMuonHits[nCands]/I");
  outTree_->Branch("muonid_dXY", &muondXY, "muonid_muondXY[nCands]/D");
  outTree_->Branch("muonid_dZ", &muondZ, "muonid_muondZ[nCands]/D");

  outTree_->Branch("Ngen"            ,&Ngen_         ,"Ngen/I"                 );
  outTree_->Branch("xsec"            ,&xsec_         ,"xsec/D"                 );

  outTree_->Branch("mZZ_type0"             ,&mZZ_type0           ,"mZZ_type0[nCands]/D"          );
  outTree_->Branch("mZZ_type1"             ,&mZZ_type1           ,"mZZ_type1[nCands]/D"          );
  outTree_->Branch("mZZ_type2"             ,&mZZ_type2           ,"mZZ_type2[nCands]/D"          );
  outTree_->Branch("mZZ_type3"             ,&mZZ_type3           ,"mZZ_type3[nCands]/D"          );
  outTree_->Branch("mZZ_type4"             ,&mZZ_type4           ,"mZZ_type4[nCands]/D"          );

  outTree_->Branch("mZZ_type0_ptUncorrected"             ,&mZZ_type0_ptUncorrected           ,"mZZ_type_ptUncorrected[nCands]/D"          );  
  outTree_->Branch("mZZ_type1_ptUncorrected"             ,&mZZ_type1_ptUncorrected           ,"mZZ_type_ptUncorrected[nCands]/D"          );  
  outTree_->Branch("mZZ_type2_ptUncorrected"             ,&mZZ_type2_ptUncorrected           ,"mZZ_type_ptUncorrected[nCands]/D"          );  
  outTree_->Branch("mZZ_type3_ptUncorrected"             ,&mZZ_type3_ptUncorrected           ,"mZZ_type_ptUncorrected[nCands]/D"          );  
  outTree_->Branch("mZZ_type4_ptUncorrected"             ,&mZZ_type4_ptUncorrected           ,"mZZ_type_ptUncorrected[nCands]/D"          );

  outTree_->Branch("pz_type0"             ,&pz_type0           ,"pz_type0[nCands]/D"          );  
  outTree_->Branch("pz_type1"             ,&pz_type1           ,"pz_type1[nCands]/D"          );  
  outTree_->Branch("pz_type2"             ,&pz_type2           ,"pz_type2[nCands]/D"          );  
  outTree_->Branch("pz_type3"             ,&pz_type3           ,"pz_type3[nCands]/D"          );  
  outTree_->Branch("pz_type4"             ,&pz_type4           ,"pz_type4[nCands]/D"          );
  outTree_->Branch("pt_neutrino"             ,&pt_neutrino           ,"pt_neutrino[nCands]/D"          );
  outTree_->Branch("pt_neutrino_corrected"             ,&pt_neutrino_corrected           ,"pt_neutrino_corrected[nCands]/D"          );
  outTree_->Branch("TOBTECjetsId"             ,&TOBTECjetsId           ,"TOBTECjetsId[nCands]/D"          );


  if(triggerNames_.size()>0){
    if(debug_)cout<<"Adding branches with trigger names"<<endl;
    //flags for telling if the event passed a certain trig path
    char triggerNamePiuI[200];
    for(unsigned int iTrig=0;iTrig<triggerNames_.size();iTrig++) {
      sprintf(triggerNamePiuI,"%s/I",(triggerNames_.at(iTrig)).c_str());
      outTree_->Branch((triggerNames_.at(iTrig)).c_str(),        &triggerRes[iTrig],       triggerNamePiuI);
    }

  }

}//end initTree()

void AnalyzerEDBR::initDataMembers(){

  lumiw  =   1.0;
  PU    =   1.0;
  PUA   =   1.0;
  PUB   =   11.0;
  genw  =   1.0;
  w     =   0.0;
  wA    =   1.0;
  wB    =   1.0;
  HLTSF =   1.0;
  BTagWeight = 1.0;
  vtagw =   1.0;
  nCands=0;
  nLooseEle=-1;
  nLooseMu=-1;

  met=0; metSign=0;  metPhi=0;          // MET and its significance
  //reset arrays
  for(int i =0 ; i < nMaxCand ; i++){

    hs[i]=-99.; h1[i]=-99.; h2[i]=-99.; phi[i]=-99.; phiS1[i]=-99.; LD[i]=-99.; 
    mzz[i]=-99.; mzzNoKinFit[i]=-99.; mll[i]=-99.; mjj[i]=-99.; mjjNoKinFit[i]=-99.;           
    ptmzz[i]=-99.; ptmzzNoKinFit[i]=-99.;
    ptlep1[i]=-99.; ptlep2[i]=-99.; etalep1[i]=-99.; etalep2[i]=-99.; philep1[i]=-99.; philep2[i]=-99.;  
    ptjet1[i]=-99.; ptjet2[i]=-99.; etajet1[i]=-99.; etajet2[i]=-99.;
    phijet1[i]=-99.; phijet2[i]=-99.;   massjet1[i]=-99.; massjet2[i]=-99.;  
    deltaREDBR[i]=-99.;
    ptZll[i]=-99.; ptZjj[i]=-99.; yZll[i]=-99.; yZjj[i]=-99.; deltaRleplep[i]=-99.; deltaRjetjet[i]=-99.;
    phiZll[i]=-99.;
    phiZjj[i]=-99.;
    btagjet1[i]=-99.;btagjet2[i]=-99.; lep[i]=-99.; reg[i]=-99.;  
    qgjet1[i]=-99.; qgjet2[i]=-99.; qgProduct[i]=-99.;   
    betajet1[i]=-99.;betajet2[i]=-99.;puMvajet1[i]=-99.;puMvajet2[i]=-99.;
    isolep1[i]=-99.; isolep2[i]=-99.; eleMVAId1[i]=-99.; eleMVAId2[i]=-99.;
    MCmatch[i]=-99.;           
    qjet[i]=-99.;tau1[i]=-99.;tau2[i]=-99.;nsubj21[i]=-99.;nsubj32[i]=-99.;
// add tau3/4/5 etc
    tau3[i]=-99.;tau4[i]=-99.; tau5[i]=-99.;
    nsubj31[i]=-99.;nsubj41[i]=-99.;nsubj51[i]=-99.;nsubj42[i]=-99.; nsubj52[i]=-99.;nsubj43[i]=-99.;nsubj53[i]=-99.;nsubj54[i]=-99.;
// add fat & sub b jet here for WH
    nfatjetbtagL[i]=-1.;nfatjetbtagM[i]=-1.;nfatjetbtagT[i]=-1.;
    nsubjetbtagL[i]=-1.;nsubjetbtagM[i]=-1.;nsubjetbtagT[i]=-1.;
// dR between two subjet 
    dR_subjet[i]=10.;
    subjet1_phi[i]=10.,subjet1_eta[i]=10.,subjet2_phi[i]=10.,subjet2_eta[i]=10.;
    subjet_flavor[i]=30;

    mdrop[i]=-99.;prunedmass[i]=-99.;
    VBFTag[i]=-999;
    VBFmJJ[i]=-999.0; VBFdeltaEta[i]=-999.0; VBFptjet1[i]=-999.0; VBFptjet2[i]=-999.0; VBFetajet1[i]=-999.0; VBFetajet2[i]=-999.0; VBFphijet1[i]=-999.0; VBFphijet2[i]=-999.0;
    mt[i]=-99.;
    nbtagsL[i]=-99.; nbtagscleanL[i]=-99.;
    nbtagsM[i]=-99.; nbtagscleanM[i]=-99.;
    nbtagsT[i]=-99.; nbtagscleanT[i]=-99.;
    isomu1mod[i]=-99.; isomu2mod[i]=-99.; 
    isoele1trk[i]=-99.; isoele2trk[i]=-99.; isoele1calo[i]=-99.; isoele2calo[i]=-99.;
    sigmaIetaIeta[i]=-99., deltaPhiSuperClusterTrackAtVtx[i]=-99., deltaEtaSuperClusterTrackAtVtx[i]=-99., hadronicOverEm[i]=-99., numberOfHits[i]=-99., dxy[i]=-99., dz[i]=-99., ecalDriven[i]=-99.,convDist[i]=-99., convDcot[i]=-99., isConv[i]=-99.,passConversionVeto[i]=-99.;
    numberOfLostHits[i]=-99.,  e1x5[i]=-99., e2x5Max[i]=-99., e5x5[i]=-99., e1x5Over5x5[i]=-99., e2x5MaxOver5x5[i]=-99.;
    globalMuon[i]=-99., nTrackerLayers[i]=-99., nPixelHits[i]=-99., nMuonHits[i]=-99., nMatches[i]=-99.;
    muondXY[i]=-99., muondZ[i]=-99.;

    nXjets[i]=-99.;	

    pz_type0[i]=-99., pz_type1[i]=-99., pz_type2[i]=-99., pz_type3[i]=-99., pz_type4[i]=-99.;
    mZZ_type0[i]=-99.,mZZ_type1[i]=-99.,mZZ_type2[i]=-99.,mZZ_type3[i]=-99.,mZZ_type4[i]=-99.;
    mZZ_type0_ptUncorrected[i]=-99.,mZZ_type1_ptUncorrected[i]=-99.,mZZ_type2_ptUncorrected[i]=-99.,mZZ_type3_ptUncorrected[i]=-99.,mZZ_type4_ptUncorrected[i]=-99.;
    pt_neutrino[i]=-99., pt_neutrino_corrected[i]=-99.;
    TOBTECjetsId[i]=-99.;
  } 


  genMassX=-999.0; genPTX=-999.0;  genYX=-999.0; genPhiX=-999.0; 
  pdgIdGenX=-999;
  genMassZll=-999.0; genPTZll=-999.0; genYZll=-999.0; genPhiZll=-999.0;
  genMassZqq=-999.0; genPTZqq=-999.0; genYZqq=-999.0; genPhiZqq=-999.0;
  genPTqP=-999.0; genEtaqP=-999.0;  genPhiqP=-999.0; 
  genPTqM=-999.0; genEtaqM=-999.0;  genPhiqM =-999.0; 
  genPTlP=-999.0; genEtalP=-999.0;  genPhilP=-999.0; 
  genPTlM=-999.0; genEtalM=-999.0;  genPhilM =-999.0; 
  genFlavqP=-999.0; genFlavqM=-999.0;
  genFlavlP=-999.0; genFlavlM=-999.0;
  genDRZqq=-99.0;genDRZll=-99.0;


}//end AnalyzeEDBR::initDataMembers()

void AnalyzerEDBR::analyzeTrigger(edm::Event const& iEvent, edm::EventSetup const& eventSetup){

  edm::Handle<edm::TriggerResults> HLTR;
  iEvent.getByLabel(edm::InputTag("TriggerResults","","HLT"), HLTR);

  for(unsigned int iTrig=0;iTrig<triggerNames_.size();iTrig++) {
    int triggerIndex = (int)hltConfig.triggerIndex((triggerNames_.at(iTrig)).c_str()) ;
    triggerRes[iTrig] = 0;
    // triggerIndex must be less than the size of HLTR or you get a CMSException: _M_range_check
    if (triggerIndex < (int)HLTR->size()) triggerRes[iTrig] = (int)HLTR->accept(triggerIndex);
  }

  //check which analysis paths the event passed.
  //this matters as we can ask for some specific things according to the 
  //path (for example electron specific quantitites for cands passing the eejj path)

  preselM_=iEvent.triggerResultsByName("CMG").accept("preselMuPath");
  finalM_= iEvent.triggerResultsByName("CMG").accept(cmgEDBRMu_);
  sbM_=false;//iEvent.triggerResultsByName("CMG").triggerIndex("cmgXZZMMSideband")!=iEvent.triggerResultsByName("CMG").size() &&     iEvent.triggerResultsByName("CMG").accept("cmgXZZMMSideband");
  preselE_=iEvent.triggerResultsByName("CMG").accept("preselElePath");
  finalE_= iEvent.triggerResultsByName("CMG").accept(cmgEDBREle_);
  sbE_=false;//iEvent.triggerResultsByName("CMG").triggerIndex("cmgXZZEESideband")!=iEvent.triggerResultsByName("CMG").size() &&  iEvent.triggerResultsByName("CMG").accept("cmgXZZEESideband");

  preselM1J_=iEvent.triggerResultsByName("CMG").accept("preselMuMergedPath");
  finalM1J_=false;// iEvent.triggerResultsByName("CMG").accept("cmgXZZMMJ");
  sbM1J_=false;//iEvent.triggerResultsByName("CMG").triggerIndex("cmgXZZMMJSideband")!=iEvent.triggerResultsByName("CMG").size() &&     iEvent.triggerResultsByName("CMG").accept("cmgXZZMMJSideband");
  preselE1J_=iEvent.triggerResultsByName("CMG").accept("preselEleMergedPath");
  finalE1J_=false;// iEvent.triggerResultsByName("CMG").accept("cmgXZZEEJ");
  sbE1J_=false;//iEvent.triggerResultsByName("CMG").triggerIndex("cmgXZZEEJSideband")!=iEvent.triggerResultsByName("CMG").size() &&  iEvent.triggerResultsByName("CMG").accept("cmgXZZEEJSideband");



  muPath_=false;
  elePath_=false;
  anyPath_=false;
  singleJetPath_=false;
  doubleJetPath_=false;
  if(preselM_ || finalM_ || sbM_||preselM1J_ || finalM1J_ || sbM1J_)muPath_=true;
  if(preselE_ || finalE_ || sbE_||preselE1J_ || finalE1J_ || sbE1J_)elePath_=true;
  if(preselE1J_ || finalE1J_ || sbE1J_|| preselM1J_ || finalM1J_ || sbM1J_ )singleJetPath_=true;
  if(preselE_ || finalE_ || sbE_|| preselM_ || finalM_ || sbM_ )doubleJetPath_=true;
  if(muPath_ || elePath_) anyPath_=true;


  //number of loose muons/electrons
  edm::Handle<std::vector<cmg::Electron> > EleHandle;
  iEvent.getByLabel("electronPreselLoose",EleHandle);
  nLooseEle = EleHandle -> size();	

  edm::Handle<std::vector<cmg::Muon> > MuHandle;
  iEvent.getByLabel("muonPreselLoose",MuHandle);	
  nLooseMu = MuHandle->size();

}//end  AnalyzeEDBR::analyzeTrigger()


void AnalyzerEDBR::analyzeGenLevel(edm::Event const& iEvent, edm::EventSetup const& eventSetup){

  //choose what to do according to user input
  bool searchX= (fillGen_>=4);  /// || fillGen_==3 || fillGen_==4);
  bool searchZll= (fillGen_==1 || fillGen_==3 || fillGen_==6 ||fillGen_==7 );
  bool searchZqq= (fillGen_==2 || fillGen_==3 || fillGen_==5 ||fillGen_==7);

  //collection of gen particles
  edm::Handle<edm::View< reco::GenParticle > > genPColl;
  iEvent.getByLabel( "genParticles"       , genPColl  );

  bool foundX=false, foundZll=false,foundZqq=false;
  //  bool foundq1=false,foundq2=false,foundl1=false,foundl2=false;
//debug
  cout<<"searchX="<<searchX<<"   foundX="<<foundX<<endl;
cout<<"genPColl->size="<<genPColl->size()<<endl;

  unsigned int i = 0;
  for( i=0;i<genPColl->size();i++){

    if( (foundX==searchX) && (foundZll==searchZll) && (foundZqq==searchZqq) )break ; //no need to continue looping
    edm::RefToBase< reco::GenParticle > genP =genPColl->refAt(i);

    int pdgId=genP->pdgId();
    int status = genP->status();
    int ndau=genP->numberOfDaughters();
//debug
//  cout<<"ndau="<<ndau<<endl;
    int pdgId_1=9999;
    if(ndau>0)pdgId_1=genP->daughter(0)->pdgId();
    int pdgId_2=9999;
    if(ndau>1)pdgId_2=genP->daughter(1)->pdgId();


    if(ndau>1  && abs(pdgId_1)==VpdgId_&& abs(pdgId_2)==VpdgId_ &&status==3){//found the X->ZZ
      foundX=true;
      genMassX=genP->mass();
      genPTX=genP->pt();
      genYX=genP->rapidity();
      genPhiX=genP->phi();
      pdgIdGenX=pdgId;
//debug
  cout<<"searchX="<<searchX<<"   foundX="<<foundX<<endl;
    }

// change here for wh analysis H->bb/cc/gg (5/4/21)
//    if(abs(pdgId)==VpdgId_ &&ndau>1 && abs(pdgId_2)<9 &&status==3){//found the V->qq
    if(abs(pdgId)==VpdgId_ &&ndau>1 && (abs(pdgId_2)==4 || abs(pdgId_2)==5 || abs(pdgId_2)==21) &&status==3){//found the V->qq
      foundZqq=true;
      genMassZqq=genP->mass();
      genPTZqq=genP->pt();
      genYZqq=genP->rapidity();
      genPhiZqq=genP->phi();
      genDRZqq=deltaR(genP->daughter(0)->phi(),genP->daughter(0)->eta(),
		      genP->daughter(1)->phi(),genP->daughter(1)->eta());

      if(genP->daughter(0)->charge()>0){//dau #0 is the positively charged quark
	genPTqP=genP->daughter(0)->pt();
	genEtaqP=genP->daughter(0)->eta();
	genPhiqP=genP->daughter(0)->phi();
	genFlavqP=int(genP->daughter(0)->pdgId());
	genPTqM=genP->daughter(1)->pt();
	genEtaqM=genP->daughter(1)->eta();
	genPhiqM=genP->daughter(1)->phi();
	genFlavqM=int(genP->daughter(1)->pdgId());
      }
      else{
	genPTqP=genP->daughter(1)->pt();
	genEtaqP=genP->daughter(1)->eta();
	genPhiqP=genP->daughter(1)->phi();
	genFlavqP=int(genP->daughter(1)->pdgId());
	genPTqM=genP->daughter(0)->pt();
	genEtaqM=genP->daughter(0)->eta();
	genPhiqM=genP->daughter(0)->phi();
	genFlavqM=int(genP->daughter(0)->pdgId());
      }
    }

    if(abs(pdgId)==VpdgId_ &&ndau>1 && status==3){//found the V->ll


      if  (abs(pdgId_2)>=11&& abs(pdgId_2)<=16){
	if  (abs(pdgId_2)>=11&&abs(pdgId_2)<=14) { 
	  foundZll=true;   
	  genMassZll=genP->mass();
	  genPTZll=genP->pt();
	  genYZll=genP->rapidity();
	  genPhiZll=genP->phi();
	  genDRZll=deltaR(genP->daughter(0)->phi(),genP->daughter(0)->eta(),
			  genP->daughter(1)->phi(),genP->daughter(1)->eta());
	}
	else if(abs(pdgId_2)==15 || abs(pdgId_2)==16){// Z->tautau or W->taunu
	  foundZll=true;  
	}

	if(genP->daughter(0)->charge()>0){//dau #0 is the positively charged quark
	  genPTlP=genP->daughter(0)->pt();
	  genEtalP=genP->daughter(0)->eta();
	  genPhilP=genP->daughter(0)->phi();
	  genFlavlP=double(genP->daughter(0)->pdgId());
	  genPTlM=genP->daughter(1)->pt();
	  genEtalM=genP->daughter(1)->eta();
	  genPhilM=genP->daughter(1)->phi();
	  genFlavlM=double(genP->daughter(1)->pdgId());
	}
	else{
	  genPTlP=genP->daughter(1)->pt();
	  genEtalP=genP->daughter(1)->eta();
	  genPhilP=genP->daughter(1)->phi();
	  genFlavlP=double(genP->daughter(1)->pdgId());
	  genPTlM=genP->daughter(0)->pt();
	  genEtalM=genP->daughter(0)->eta();
	  genPhilM=genP->daughter(0)->phi();
	  genFlavlM=double(genP->daughter(0)->pdgId());
	}

      }
    }



  }//end loop on genParticles

// debug
  cout<<"searchX="<<searchX<<"   foundX="<<foundX<<endl;
  if( searchX && (!foundX) ) std::cout<<"WARNING from AnalyzerEDBR::analyzeGenLevel!!! Loop on genLevel particles ended without having found X->VV "<<std::endl;
  if( searchZqq && (!foundZqq) ) std::cout<<"WARNING from AnalyzerEDBR::analyzeGenLevel!!! Loop on genLevel particles ended without having found V->qq "<<std::endl;
  if( searchZll && (!foundZll) ) std::cout<<"WARNING from AnalyzerEDBR::analyzeGenLevel!!! Loop on genLevel particles ended without having found V->leplep "<<std::endl;


}//end AnalyzerEDBR::analyzeGenLevel

double AnalyzerEDBR::deltaR(reco::LeafCandidate p1,reco::LeafCandidate p2){
  double deltaEta = fabs(p1.eta()-p2.eta());
  double deltaPhi = (p1.phi()-p2.phi());
  while (deltaPhi > 3.14) deltaPhi -= 2*3.14;
  while (deltaPhi <= -3.14) deltaPhi += 2*3.14;     
  return sqrt(deltaPhi*deltaPhi + deltaEta*deltaEta);
}
double AnalyzerEDBR::deltaR(double phi1,double eta1,double phi2,double eta2){
  double deltaEta = fabs(eta1-eta2);
  double deltaPhi = (phi1-phi2);
  while (deltaPhi > 3.14) deltaPhi -= 2*3.14;
  while (deltaPhi <= -3.14) deltaPhi += 2*3.14;     
  return sqrt(deltaPhi*deltaPhi + deltaEta*deltaEta);
}



#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnalyzerEDBR);
