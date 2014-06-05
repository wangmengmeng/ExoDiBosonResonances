/** \macro H2GGFitter.cc
 *
 * $Id: R2JJFitter.cc,v 1.2 2013/06/07 09:28:04 tomei Exp $
 *
 * Software developed for the CMS Detector at LHC
 *
 *
 *  \author Serguei Ganjour - CEA/IRFU/SPP, Saclay
 *  \modified by Maxime Gouzevitch for the Dijet Bump Search - IPNL, Lyon 
 *
 * Macro is implementing the unbinned maximum-likelihood model for 
 * the Higgs to gamma gamma analysis. PDF model and RooDataSets 
 * are stored in the workspace which is feeded to  HiggsAnalysis/CombinedLimit tools:
 * 
 * http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/HiggsAnalysis/CombinedLimit
 * http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/HiggsAnalysis/CombinedLimit/data/lhc-hcg/cms-hgg-1fb/
 * 
 * The analysis root trees produced in a simple format 
 *
 *     TFile file(filename,"RECREATE", "X->jj input tree for unbinned maximum-likelihood fit");
 *     TTree* outTree  = new TTree("XTojj","X->jj input tree for unbinned maximum-likelihood fit");
 *     Float_t mass;
 *     Int_t CAT3;
 *     Float_t weight;
 *
 *     outTree->Branch("mass",&mass,"mass/F");
 *     outTree->Branch("weight",&weight,"weight/F");
 *     outTree->Branch("CAT4",&CAT4,"CAT4/I");
 *     {
 *       .............
 *       outTree->Fill();
 *     }
 *
 *     file.Write();
 *     file.Close();
 *     delete outTree;
 *
 * are used as input files. They have to be produced for 
 * data and Monte Carlo signal and background data sets 
 * after all analysis selections to be applied. It is recommended to put   
 * loose kinematical cuts on pt1 and pt2 (20 GeV) since further selections 
 * are possible based on RooDataSets. 
 * It is recommended to use Root 5.28/00 (CMSSW_4_1_3).
 *
 *
 */
// Loading:  .L H2GGFitter.cc
// Running:  runfits("hgg120-shapes-combined-Unbinned.root")  
//                

/*
#include <cstring>
#include <cerrno>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <stdexcept>
#include <algorithm>
#include <unistd.h>
#include <errno.h>
#include <iomanip>
// ROOT headers
#include "TCanvas.h"
#include "TAxis.h"
#include "TH1F.h"
#include "TF1.h"
#include "TFile.h"
#include "TTree.h"
#include "TIterator.h"

#include "TLatex.h"
#include "TString.h"
#include "TLegend.h"
#include "TGraphAsymmErrors.h"


// RooFit headers
#include "RooAbsPdf.h"
#include "RooDataHist.h"
#include "RooDataSet.h"
#include "RooHistPdf.h"
#include "RooMsgService.h"
#include "RooNLLVar.h"
#include "RooPlot.h"
#include "RooRandom.h"
#include "RooRealVar.h"
#include "RooWorkspace.h"
#include "TStyle.h"

// RooStats headers
#include "RooStats/HLFactory.h"

#include "RooAbsPdf.h"
#include "RooAddPdf.h"
#include "RooProdPdf.h"
#include "RooAbsData.h"
#include "RooPlot.h"
#include "RooGaussian.h"
#include "RooProduct.h"
#include "RooExtendPdf.h"
#include "RooBernstein.h"
#include "RooFitResult.h"
#include "RooMinimizer.h"
#include "RooCmdArg.h"
#include "RooConstVar.h"
#include "RooRealVar.h"
*/
//#include "HiggsCSandWidth.h"
//#include "HiggsCSandWidth.cc"
//#include "RooPower.h"

#include <sstream>
using namespace RooFit;
using namespace RooStats ;

static const Int_t NCAT = 4;
static const Double_t MMIN = 500;
static const Double_t MMAX = 2800;

void AddSigData(RooWorkspace*, Float_t);
void AddBkgData(RooWorkspace*);
void SigModelFit(RooWorkspace*, Float_t);
void SigModelSet(RooWorkspace*, double*, int);
RooFitResult*  BkgModelFitBernstein(RooWorkspace*, Bool_t);
void MakePlots(RooWorkspace*, Float_t, RooFitResult* , bool);
void MakeSigWS(RooWorkspace* w, const char* filename);
void MakeBkgWS(RooWorkspace* w, const char* filename);
void SetParamNames(RooWorkspace*);
void SetConstantParams(const RooArgSet* params);


RooArgSet* defineVariables()
{

  // define variables of the input ntuple
  RooRealVar* mZZ  = new RooRealVar("mZZ","M(VV)",MMIN,MMAX,"GeV");
  RooRealVar* weight   = new RooRealVar("weight","Reweightings",0,100000,"");
  RooRealVar* region   = new RooRealVar("region","jet mass region",-3,3,"");
  // Adapting to ZZ trees
  //RooCategory* categories = new RooCategory("categories","event category 4") ;
  //categories->defineType("VV_mass_ele_LP",0);
  //categories->defineType("VV_mass_ele_HP",1);
  //categories->defineType("VV_mass_mu_LP",2);
  //categories->defineType("VV_mass_mu_HP",3);
  RooCategory* leptonFlavour = new RooCategory("lep","Lepton Flavour");
  RooCategory* taggingPurity = new RooCategory("vTagPurity","Tagging Purity");
  leptonFlavour->defineType("electron",0);
  leptonFlavour->defineType("muon",1);
  taggingPurity->defineType("lowPurity",0);
  taggingPurity->defineType("highPurity",1);
  //   categories->defineType("dijet_mass_1mtag_1mdtag",4);
  //   categories->defineType("dijet_mass_0mtag",5);

  //RooArgSet* ntplVars = new RooArgSet(*mZZ, *categories, *weight, *region);
  RooArgSet* ntplVars = new RooArgSet(*mZZ, *leptonFlavour, *taggingPurity, *weight, *region);
  return ntplVars;
}



void runfits(const Float_t mass=1000, bool isWW = true, Bool_t dobands = false)
{

  //******************************************************************//
  //  Running mode  corresponds to the following cases
  //         - full run set:
  //         - create signal and background data sets 
  //         - make and fit signal and background  models 
  //         - write signal and background workspaces in root files
  //         - write data card

  //*******************************************************************//

  TString fileBaseName(TString::Format("Xvv.mX%d_ZZ_8TeV", int(mass)));
  if (isWW) fileBaseName = TString::Format("Xvv.mX%d_WW_8TeV", int(mass));

  TString fileBkgName(TString::Format("Xvv.inputbkg_8TeV", mass));
  TString card_name("Xvv_models_Bkg_8TeV_test.rs");
  HLFactory hlf("HLFactory", card_name, false);
  RooWorkspace* w = hlf.GetWs();
  RooFitResult* fitresults;

  // Add data to the workspace
  AddSigData(w, mass, isWW);
  cout << "AddSigData() done!" << endl;
  
  AddBkgData(w);
  cout << "AddBkgData() done!" << endl;
  
  // Fit with models
  SigModelFit(w, mass);
  cout << "SigModelFit() done!" << endl;
  fitresults = BkgModelFitBernstein(w, dobands);
  cout << "BkgModelFitBernstein() done!" << endl;
      
  // Create Workspaces
  MakeSigWS(w, fileBaseName);
  cout << "MakeSigWS() done!" << endl;
  MakeBkgWS(w, fileBkgName);
  cout << "MakeBkgWS() done!" << endl;

  // Make datacards for "combine" tool
  int ncat = NCAT;
  for (int c = 0; c < ncat; c++) 
    MakeDataCard_1Channel(w, fileBaseName, fileBkgName, c, mass);
  
  cout << "MakeDataCard() done!" << endl;
  /*
  // Make plots for data and fit results
  MakePlots(w, mass, fitresults, isWW);
  */

  return;
}



void AddSigData(RooWorkspace* w, Float_t mass, bool isWW) {

  TString inDir   = "/afs/cern.ch/work/t/tomei/public/EXOVV_2012/unrolled_trees_v2c/";
  
  int iMass = abs(mass);       
  /*
  TFile sigFile1(inDir+TString(Form("dijetWtag_Moriond_ZZHppOUT%d_miniTree.root", iMass)));  
  if (isWW) {
    sigFile1.Close();
    TFile sigFile1(inDir+TString(Form("dijetWtag_Moriond_WWHppOUT%d_miniTree.root", iMass)));
  }
  */                     

  /// Why we need the SIGNAL here???
  //TFile sigFile1(inDir+TString(Form("treeEDBR_BulkG_WW_lvjj_c0p2_M%d_xww.root", iMass)));
  //EXOVVTree_BulkG_ZZ_lljj_c0p2_M1700_SIG_NOcut.root
 
  /// A bit of workaround. I don't want to change the inner workings of the script.
  /// If we're dealing with a mass point for which we have no MC... we just open another file
  int iMassOfFileToOpen; 
  if(iMass%100 == 0) 
    iMassOfFileToOpen=iMass;
  else
    iMassOfFileToOpen=(iMass-iMass%100);
      
  cout << "iMassOfFileToOpen = " << iMassOfFileToOpen << endl;

  TFile sigFile1(inDir+TString(Form("EXOVVTree_BulkG_ZZ_lljj_c0p2_M%d_SIG.root", iMassOfFileToOpen)));
  
  /*
  if (!isWW) {
    TFile sigFile1(inDir+TString(Form("treeEDBR_BulkG_ZZ_lljj_c0p2_M%d_xww.root", iMass)));  
  }

  if (isWW) {
    //sigFile1.Close();
    TFile sigFile1(inDir+TString(Form("treeEDBR_BulkG_WW_lvjj_c0p2_M%d_xww.root", iMass)));
  }
  */

  // common preselection cut
  //TString mainCut("1");
  TString mainCut("region==1"); //sideband + ignore 2jet categories (for the moment)

  // Luminosity:
  Float_t Lum = 19770.0;
  RooRealVar lumi("lumi","lumi",Lum);
  w->import(lumi); 

  Int_t ncat = NCAT;  
  Float_t MASS(mass);
  //Float_t sqrts(8);

  //HiggsCSandWidth *myCSW = new HiggsCSandWidth();

  //Float_t xs_ggqq  = 0.05;
  //Float_t br       = 1.0;

  /*
  cout << "++++++++++++++++++++++++++++++++" << endl;
  cout << "sigma_X x BR (mX = " << MASS << ") = "  << xs_ggqq*br << endl;
  cout << "++++++++++++++++++++++++++++++++" << endl;
  */

  // number of generated events in each signal dataset
  //Float_t n_ggqq(30000);

  // Scale factor for the signal
  //Float_t scaleX  = lumi.getVal()*xs_ggqq * br /n_ggqq;

  TTree* sigTree1 = (TTree*) sigFile1.Get("SelectedCandidatesV2");
  if(sigTree1==0) {
    cout << endl; 
    cout << "================================================================" << endl;
    cout << "The sigTree1 in AddSigData is 0... aborting." << endl;
    cout << "================================================================" << endl;
    cout << endl;
    abort();
  }
  

  // Variables
  RooArgSet* ntplVars = defineVariables();
  RooRealVar weightVar("weightVar","",1,0,1000);

  // add weight var into the list of ntuple variables
  weightVar.setVal(1.);
  ntplVars->add(RooArgList(weightVar));

  //****************************//
  // Signal  Data Set
  //****************************//

  // Create non scaled signal dataset composed with  different productions 
  // according to their cross sections

  //NOTE: it seems that "sigScaled" and "Sig_cat" are actually never really used..

  cout << "=========" << endl;
  ntplVars->Print();
  cout << "=========" << endl;


  cout << "=========" << endl;
  cout << "========= sigScaled" << endl;
  cout << "=========" << endl;
  
  /// If it's not used, why do we make it?
  RooDataSet sigScaled("sigScaled","dataset",sigTree1,*ntplVars,mainCut,"weight");
  
  //RooDataSet sigScaled("sigScaled","dataset",sigTree1,*ntplVars,mainCut); //NO WEIGHTS
  
  ///sigScaled.Print("v");

  cout << "=========" << endl;
  cout << "========= sigToFit vs category" << endl;
  cout << "=========" << endl;
  RooDataSet* sigToFit[NCAT];
  for (int c = 0; c < ncat; ++c) {
    int calculatedLep = c/2;
    int calculatedVT = c%2;
    
    cout << "Trying now with c==" << c <<endl;
    TString theCut = mainCut+TString::Format(" && lep==%d && vTagPurity==%d",
					     calculatedLep,calculatedVT);
    cout << "Using cut: " << endl;
    cout << theCut.Data() << endl;
    sigToFit[c] =  (RooDataSet*) sigScaled.reduce(*w->var("mZZ"),theCut);
    w->import(*sigToFit[c],Rename(TString::Format("Sig_cat%d",c)));
    sigToFit[c]->Print("v");
  }
  
  w->Print();
          
  // Create full signal data set without categorization
  cout << "=========" << endl;
  cout << "========= sigToFitAll" << endl;
  cout << "=========" << endl;
  RooDataSet* sigToFitAll  = (RooDataSet*) sigScaled.reduce(*w->var("mZZ"),mainCut);
  w->import(*sigToFitAll,Rename("Sig"));
  sigToFitAll->Print("v");

  // Create weighted signal dataset composed with  different 
  // production processes according to their cross sections
  // no common preselection cut applied yet 

  //---
  //RooRealVar *weightVar1 = (RooRealVar*) (*ntplVars)["weight"] ;
  //RooRealVar *weightVar2 = (RooRealVar*) (*ntplVars)["normWeight"] ;
  //RooFormulaVar *weightVar3 = new RooFormulaVar( "weight3", "", "@0", RooArgList(*weightVar1));
  //---
  //weightVar.setVal(1.);
  //ntplVars->setRealValue("normWeight", scaleX);
  //RooDataSet sigWeightedTmp1("sigData","dataset",sigTree1,*ntplVars,mainCut,"weightVar");
  //RooRealVar *weightX = (RooRealVar*) sigWeightedTmp1.addColumn(*weightVar3) ;
  //   RooDataSet sigWeighted("sigData","dataset",
  // 			 RooArgList((*ntplVars)["mZZ"],
  // 				    (*ntplVars)["categories"],*weightX),
  // 			 Import(sigWeightedTmp1),WeightVar(*weightX));
  //---

  cout << "=========" << endl;
  cout << "========= sigWeighted" << endl;
  cout << "=========" << endl;
  RooDataSet sigWeighted("sigData","dataset",sigTree1,*ntplVars,mainCut,"weight");
  //RooDataSet sigWeighted("sigData","dataset",sigTree1,*ntplVars,mainCut); //NO WEIGHTS
  sigWeighted.Print("v");

  /*
  cout << "---- nX:  " << sigWeighted.sumEntries() << endl; 
  for (int c = 0; c < ncat; ++c) {
    Float_t nExpEvt = sigWeighted.reduce(*w->var("mZZ"),TString::Format("categories==%d",c))->sumEntries();
    cout << TString::Format("nEvt exp.  cat%d : ",c) << nExpEvt 
	 << TString::Format("   eff x Acc  cat%d : ",c) << nExpEvt*100/scaleX/100000. << "%"  
	 << endl; 
  }
  */

  cout << "=========" << endl;
  cout << "========= signal vs category" << endl;
  cout << "=========" << endl;
  RooDataSet* signal[NCAT];
  for (int c = 0; c < ncat; ++c) {
    /// Magic!!! Translate the value of "c" into the correct values of lep and vTagPurity.
    ///categories->defineType("VV_mass_ele_LP",0);
    ///categories->defineType("VV_mass_ele_HP",1);
    ///categories->defineType("VV_mass_mu_LP",2);
    ///categories->defineType("VV_mass_mu_HP",3);
    int calculatedLep = c/2;
    int calculatedVT = c%2;
    signal[c] =  (RooDataSet*) sigWeighted.reduce(*w->var("mZZ"),mainCut+TString::Format(" && lep==%d && vTagPurity==%d",
											 calculatedLep,calculatedVT));
    w->import(*signal[c],Rename(TString::Format("SigWeight_cat%d",c)));
    signal[c]->Print("v");
  }

  // Create full weighted signal data set without categorization
  cout << "=========" << endl;
  cout << "========= signalAll" << endl;
  cout << "=========" << endl;
  RooDataSet* signalAll  = (RooDataSet*) sigWeighted.reduce(*w->var("mZZ"),mainCut);
  w->import(*signalAll, Rename("SigWeight"));

}


void AddBkgData(RooWorkspace* w) {

  //TString inDir   = "/afs/cern.ch/user/b/bonato/public/unrolled_trees_prodv2c/";
  TString inDir   = "/afs/cern.ch/work/t/tomei/public/EXOVV_2012/unrolled_trees_v2c/";
  TFile dataFile(inDir+"EXOVVTree_DATASIG_NOcut.root");
  
  // common preselection cut
  //TString mainCut("1");
  //TString mainCut("region==1 && categories>=0 && categories<4"); //sideband + ignore 2jet categories (for the moment)
  TString mainCut("region==1"); //sideband + ignore 2jet categories (for the moment)
  Int_t ncat = NCAT;
  Float_t minMassFit(MMIN),maxMassFit(MMAX); 

  TTree* dataTree     = (TTree*) dataFile.Get("SelectedCandidatesV2");
  if(dataTree==0) {
    cout << endl; 
    cout << "================================================================" << endl;
    cout << "The dataTree in AddBkgData is 0... aborting." << endl;
    cout << "================================================================" << endl;
    cout << endl;
    abort();
  }
  
  // Variables
  RooArgSet* ntplVars = defineVariables();

  // Apply a common preselection cut;
  cout << "=========" << endl;
  cout << "========= Data" << endl;
  cout << "=========" << endl;

  //============== IMPORTANT ==========================

  //--
  // For real data
  RooDataSet Data("Data","dataset",dataTree,*ntplVars,mainCut,"weight");
  //--

  //--
  // For MC background
  //
  //Float_t LumForBkg = 19500.0;
  //RooRealVar lumiForBkg ("lumiForBkg","lumiForBkg",LumForBkg);  
  //
  //RooRealVar *weightOriginal = (RooRealVar*) (*ntplVars)["weight"] ;
  //RooFormulaVar *weightNormLumiFormula = new RooFormulaVar("weightNormLumiFormula","","@0*@1",RooArgList(*weightOriginal, lumiForBkg));    
  //
  //RooDataSet *DataNoWeight = new RooDataSet("DataNoWeight","DataNoWeight",dataTree,*ntplVars,mainCut);
  //RooRealVar *weightFinal = (RooRealVar*) DataNoWeight->addColumn(*weightNormLumiFormula) ;
  //RooDataSet Data("Data","dataset",DataNoWeight,*DataNoWeight->get(),mainCut,weightFinal->GetName());
  //--

  //====================================================

  Data.Print("v");

  // split into NCAT  categories;  
  cout << "=========" << endl;
  cout << "========= dataToFit vs category" << endl;
  cout << "=========" << endl;
  RooDataSet* dataToFit[NCAT];
  for (int c = 0; c < ncat; ++c) {
    // Real data
    int calculatedLep = c/2;
    int calculatedVT = c%2;
    dataToFit[c]   = (RooDataSet*) Data.reduce(*w->var("mZZ"),mainCut+TString::Format(" && vTagPurity==%d && lep==%d",calculatedVT,calculatedLep));
    w->import(*dataToFit[c],Rename(TString::Format("Data_cat%d",c)));
    dataToFit[c]->Print("v");
  }

  // Create full data set without categorization
  cout << "=========" << endl;
  cout << "========= data (same as -Data-?)" << endl;
  cout << "=========" << endl;
  RooDataSet* data  = (RooDataSet*) Data.reduce(*w->var("mZZ"),mainCut);
  w->import(*data, Rename("Data"));
  data->Print("v");

}

void ReadFromFile(ifstream& myfile, double* params) {
  /* File structure
     mean_match =  606.57 +/- 254.58 L(400 - 800) 
     sigma_match =  22.978 +/- 48.225 L(20 - 70) 
     width_match =  1.0000 L(0 - 1000) 
     mean_unmatch =  600.00 C L(200 - 1500) 
     sigma_unmatch =  30.000 C L(1 - +INF) 
     alpha_unmatch =  1.0000 C L(-INF - +INF) 
     n_unmatch =  0.30000 C L(0 - 20) 
     machfrac =  0.99900 C L(0 - 1) 
     alpha1_match =  2.2912 +/- 2.5776 L(0.01 - 5) 
     n1_match =  1.7910 +/- 5.4302 L(0 - 10) 
     alpha2_match =  2.3328 +/- 3.1736 L(0.01 - 5) 
     n2_match =  1.8134 +/- 7.7558 L(0 - 10) 
  */
    string line; // Line of the input file
    string buf; // Have a buffer string
    stringstream ss; // Insert the string into a stream
    double value;
    if (myfile.is_open()) {
      // Ok, file is open.
      getline (myfile,line); /// mean_match
      ss.str(line); ss >> buf; ss >> buf; ss >> buf; value = atof(buf.c_str()); params[0]=value;
      getline (myfile,line); /// sigma_match
      ss.str(line); ss >> buf; ss >> buf; ss >> buf; value = atof(buf.c_str()); params[1]=value;
      getline (myfile,line); /// width_match (discard)
      getline (myfile,line); /// mean_unmatch (discard)
      getline (myfile,line); /// sigma_unmatch (discard)
      getline (myfile,line); /// alpha_unmatch (discard)
      getline (myfile,line); /// n_unmatch (discard)
      getline (myfile,line); /// machfrac (discard)
      getline (myfile,line); /// alpha1_match
      ss.str(line); ss >> buf; ss >> buf; ss >> buf; value = atof(buf.c_str()); params[2]=value;
      getline (myfile,line); /// n1_match
      ss.str(line); ss >> buf; ss >> buf; ss >> buf; value = atof(buf.c_str()); params[3]=value;
      getline (myfile,line); /// alpha2_match
      ss.str(line); ss >> buf; ss >> buf; ss >> buf; value = atof(buf.c_str()); params[4]=value;
      getline (myfile,line); /// n2_match
      ss.str(line); ss >> buf; ss >> buf; ss >> buf; value = atof(buf.c_str()); params[5]=value;
    }
    else {
      printf("WHAT THE FLYING FUCK MY FILE IS NOT OPEN!!!\n");
    }
    myfile.close();  
}

void SigModelSet(RooWorkspace* w, double* params, int c) {
  w->var(TString::Format("mgg_sig_m0_cat%d",c))->setVal(params[0]);
  w->var(TString::Format("mgg_sig_sigma_cat%d",c))->setVal(params[1]);
  w->var(TString::Format("mgg_sig_alpha1_cat%d",c))->setVal(params[2]);
  w->var(TString::Format("mgg_sig_n1_cat%d",c))->setVal(params[3]);
  w->var(TString::Format("mgg_sig_alpha2_cat%d",c))->setVal(params[4]);
  w->var(TString::Format("mgg_sig_n2_cat%d",c))->setVal(params[5]);
}

void SigModelFit(RooWorkspace* w, Float_t mass) {

  Int_t ncat = NCAT;
  Float_t MASS(mass);

  //******************************************//
  // Fit signal with model pdfs
  //******************************************//
  // retrieve pdfs and datasets from workspace to fit with pdf models

  RooDataSet* sigToFit[NCAT];
  RooAbsPdf* MggSig[NCAT];

  Float_t minMassFit(MMIN),maxMassFit(MMAX); 

  // Fit Signal 
  for (int c = 0; c < ncat; ++c) {
  //for (int c = 1; c < 4; ++c) {

    cout << "---------- category = " << c << endl;
    //    sigToFit[c]   = (RooDataSet*) w->data(TString::Format("Sig_cat%d",c));
    sigToFit[c]   = (RooDataSet*) w->data(TString::Format("SigWeight_cat%d",c));
    MggSig[c]     = (RooAbsPdf*)  w->pdf(TString::Format("MggSig_cat%d",c));

    /// Unlike the WW case, we don't sum a gaussian. We use a pure Double Crystal Ball.
    ((RooRealVar*) w->var(TString::Format("mgg_sig_m0_cat%d",c)))->setVal(MASS);  
    //((RooRealVar*) w->var(TString::Format("mgg_sig_gsigma_cat%d",c)))->setVal(MASS*0.1); ---> So this doesn't exist 
    ((RooRealVar*) w->var(TString::Format("mgg_sig_sigma_cat%d",c)))->setVal(MASS*0.1);  
    cout << "---------------- Peak Val = " << w->var(TString::Format("mgg_sig_m0_cat%d",c))->getVal() << " Mass = " << MASS << endl;

    //define a set with the parameters
    w->defineSet(TString::Format("SigPdfParam_cat%d",c), RooArgSet(*w->var(TString::Format("mgg_sig_m0_cat%d",c)),
								   *w->var(TString::Format("mgg_sig_sigma_cat%d",c)),
								   *w->var(TString::Format("mgg_sig_alpha1_cat%d",c)),
								   *w->var(TString::Format("mgg_sig_n1_cat%d",c)), 
								   *w->var(TString::Format("mgg_sig_alpha2_cat%d",c)),
								   *w->var(TString::Format("mgg_sig_n2_cat%d",c))));
    //read initial values from text file
    //w->set(TString::Format("SigPdfParam_cat%d",c))->readFromFile(TString::Format("SigPdfParam/SigPdfParamLast_%d_cat%d.dat",(int)MASS,c));
    int leptonCategory = c/2;
    int VTagPurity = c%2; /// Irrelevant, not used
    int nxj = 1; /// We're doing the 1-jet case only.
    /// outpars_BulkG_ZZ_lljj_c0p2_M2000_1J__MU.config
    std::string leptType_str = (leptonCategory==0)?"ELE":"MU";

    /// Let's read from the file!
    /// There SHOULD be a smarter way to do this....
    /// First: do we actually have a file for this?
    int iMass = (int)MASS;
    bool weHaveAFileForThis = ((iMass%100)==0);
    
    if(weHaveAFileForThis) {
      /// Ok, open and read the file
      double params[6];
      ifstream myfile(TString::Format("../fits/shape/pars/outpars_BulkG_ZZ_lljj_c0p2_M%d_%dJ__%s.config",
				      iMass,
				      nxj,
				      leptType_str.c_str()));
      ReadFromFile(myfile, params);
      SigModelSet(w, params, c);
    }  
    else {
      cout << "Try to interpolate" << endl;
      /// Ok, open the two neighbouring files and average the values (LOL?)
      double params[6];
      double paramslow[6];
      double paramshigh[6];
      int lowTag = iMass-50;
      int highTag = iMass+50;
      ifstream myfileLow(TString::Format("../fits/shape/pars/outpars_BulkG_ZZ_lljj_c0p2_M%d_%dJ__%s.config",
					 lowTag,
					 nxj,
					 leptType_str.c_str()));
      ifstream myfileHigh(TString::Format("../fits/shape/pars/outpars_BulkG_ZZ_lljj_c0p2_M%d_%dJ__%s.config",
					  highTag,
					  nxj,
					  leptType_str.c_str()));
      ReadFromFile(myfileLow, paramslow);
      ReadFromFile(myfileHigh, paramshigh);
      for(int ii=0; ii!=6; ++ii) {
	params[ii] = (paramslow[ii]+paramshigh[ii])/2.0;
      }
      SigModelSet(w, params, c);
    }
    
    
    //MggSig[c]     ->fitTo(*sigToFit[c],Range(minMassFit,maxMassFit),SumW2Error(kTRUE));
    printf("We are in SigModelFit, c = %i\n",c);
    /// This is the fit we DON'T want to do...
    bool redoFit = false;
    if(redoFit) {
      MggSig[c]     ->fitTo(*sigToFit[c],Range( TMath::Max(minMassFit,MASS-2.5*MASS*0.1) , MASS+2.5*MASS*0.1 ),SumW2Error(kTRUE));
    }

    w->set(TString::Format("SigPdfParam_cat%d",c))->Print();
    w->var(TString::Format("mgg_sig_m0_cat%d",c))->Print();
    w->var(TString::Format("mgg_sig_sigma_cat%d",c))->Print();
    w->var(TString::Format("mgg_sig_alpha1_cat%d",c))->Print();
    w->var(TString::Format("mgg_sig_n1_cat%d",c))->Print();
    w->var(TString::Format("mgg_sig_alpha2_cat%d",c))->Print();
    w->var(TString::Format("mgg_sig_n2_cat%d",c));

    //write new fit results to file
    w->set(TString::Format("SigPdfParam_cat%d",c))->writeToFile(TString::Format("SigPdfParam/SigPdfParamNew_%d_cat%d.dat",(int)MASS,c));

    // IMPORTANT: fix all pdf parameters to constant
    SetConstantParams(w->set(TString::Format("SigPdfParam_cat%d",c)));

    //=== Plots --> MOVE THIS PART IN THE APPROPRIATE AREA?
    //---> RooRealVar *weightVar1 = (RooRealVar*) (*ntplVars)["weight"] ;
    // retrieve mass observable from the workspace
    RooRealVar* massForPlot     = w->var("mZZ");  
    massForPlot->setUnit("GeV");
    Int_t nBinMass(40);
    RooPlot* myframe = massForPlot->frame(nBinMass) ;
    sigToFit[c]->plotOn(myframe) ;
    MggSig[c]->plotOn(myframe) ;
    MggSig[c]->plotOn(myframe
		      //,
		      //Components(TString::Format("MggGaussSig_cat%d",c)),
		      //Components(TString::Format("MggCBSig_cat%d",c)),
		      //LineStyle(kDashed)
		      );
    MggSig[c]->paramOn(myframe,sigToFit[c]);
    TCanvas* canvas = new TCanvas("canvas","canvas",1200,400);
    myframe->Draw();
    canvas->SaveAs(TString::Format("plots/SignalShape_m%d_cat%d.png",int(MASS),c));
    delete canvas;

  }

  //  w->pdf("MggSig")->fitTo(*w->data("Sig"), Range(minMassFit,maxMassFit),SumW2Error(kTRUE));
}



RooFitResult* BkgModelFitBernstein(RooWorkspace* w, Bool_t dobands) {

  Int_t ncat = NCAT;

  std::vector<TString> catdesc;
  catdesc.push_back("#scale[0.8]{WW_mass_ele_LP}");
  catdesc.push_back("#scale[0.8]{WW_mass_ele_HP}");
  catdesc.push_back("#scale[0.8]{WW_mass_mu_LP}");
  catdesc.push_back("#scale[0.8]{WW_mass_mu_HP}");


  //******************************************//
  // Fit background with model pdfs
  //******************************************//

  // retrieve pdfs and datasets from workspace to fit with pdf models


  RooDataSet* data[NCAT];
  RooBernstein* MggBkg[NCAT];
  RooFitResult* fitresult[NCAT];;
  RooPlot* plotMggBkg[NCAT];

  // dobands and dosignal
  RooDataSet* signal[NCAT];
  RooAbsPdf*  MggSig[NCAT];


  Float_t minMassFit(MMIN),maxMassFit(MMAX); 

  // Fit data with background pdf for data limit

  RooRealVar* mgg     = w->var("mZZ");  
  mgg->setUnit("GeV");
  
  TLatex *text = new TLatex();
  text->SetNDC();
  text->SetTextSize(0.04);

  for (int c = 0; c < ncat; ++c) {
    data[c]   = (RooDataSet*) w->data(TString::Format("Data_cat%d",c));
    
    //parameter 3 set to constant            
    ((RooRealVar*) w->var(TString::Format("mgg_bkg_8TeV_slope3_cat%d",c)))->setConstant(true);
    cout << "---------------- Parameter 3 set to const" << endl;
    
    RooFormulaVar *p1mod = new RooFormulaVar(TString::Format("p1mod_cat%d",c),"","@0",*w->var(TString::Format("mgg_bkg_8TeV_slope1_cat%d",c)));
    RooFormulaVar *p2mod = new RooFormulaVar(TString::Format("p2mod_cat%d",c),"","@0",*w->var(TString::Format("mgg_bkg_8TeV_slope2_cat%d",c)));
    RooFormulaVar *p3mod = new RooFormulaVar(TString::Format("p3mod_cat%d",c),"","@0",*w->var(TString::Format("mgg_bkg_8TeV_slope3_cat%d",c)));

    //--
    //shape
    //--
    //-- Standard di-jet function
    //     RooFormulaVar *sqrtS = new RooFormulaVar(TString::Format("sqrtS_cat%d",c),"","@0",*w->var("sqrtS"));
    //     RooFormulaVar *x = new RooFormulaVar(TString::Format("x_cat%d",c),"","@0/@1",RooArgList(*mgg, *sqrtS));    
    //     RooAbsPdf* MggBkgTmp0 = new RooGenericPdf(TString::Format("DijetBackground_%d",c), "pow(1-@0, @1)/pow(@0, @2+@3*log(@0))", RooArgList(*x, *p1mod, *p2mod, *p3mod)); 

    //-- Leveled exponential 
    //   y = exp( -x / ( sigma + alpha*x + beta*x^2 ) )
    RooFormulaVar *xNoScale = new RooFormulaVar(TString::Format("x_NoScale_cat%d",c),"","@0",RooArgList(*mgg));    
    RooAbsPdf* MggBkgTmp0 = new RooGenericPdf(TString::Format("LevelExpoBackground_%d",c), "exp(- @0 / (@1 + @2*@0 + @3*@0*@0) )", RooArgList(*xNoScale, *p1mod, *p2mod, *p3mod)); 
    //RooAbsPdf* MggBkgTmp0 = new RooGenericPdf(TString::Format("LevelExpoBackground_%d",c), "exp(- @0 / (@1 + @2*@0) )", RooArgList(*xNoScale, *p1mod, *p2mod)); 
    //
    //

    //--
    //normalization
    //--
    w->factory(TString::Format("mgg_bkg_8TeV_norm_cat%d[4000.0,0.0,10000000]",c));
    RooExtendPdf MggBkgTmp(TString::Format("MggBkg_cat%d",c),"",*MggBkgTmp0,*w->var(TString::Format("mgg_bkg_8TeV_norm_cat%d",c)));

    fitresult[c] = MggBkgTmp.fitTo(*data[c], Strategy(1),Minos(kFALSE), Range(minMassFit,maxMassFit),SumW2Error(kTRUE), Save(kTRUE));
    w->import(MggBkgTmp);

    //************************************************//
    // Plot Mgg background fit results per categories 
    //************************************************//
    // Plot Background Categories 
    //****************************//

    TCanvas* ctmp = new TCanvas("ctmp","M(VV) Background Categories",0,0,500,500);
    Int_t nBinsMass(20);
    plotMggBkg[c] = mgg->frame(nBinsMass);

    //data[c]->plotOn(plotMggBkg[c],LineColor(kWhite),MarkerColor(kWhite)); //not needed?
    data[c]->plotOn(plotMggBkg[c]);    
    data[c]->statOn(plotMggBkg[c]) ;
    MggBkgTmp.plotOn(plotMggBkg[c],LineColor(kBlue),Range("fitrange"),NormRange("fitrange")); 
    MggBkgTmp.paramOn(plotMggBkg[c],data[c],"",2,"NELU",0.356855,0.877016,0.741525);
    plotMggBkg[c]->Draw();
    plotMggBkg[c]->SetMinimum(0.1);    

    Double_t chi2 = plotMggBkg[c]->chiSquare(3);
    char Chi2Text[55]; 
    sprintf(Chi2Text,"Chi2/ndf = %f",chi2); 
    TLatex *texf = new TLatex( 2190.32,8.70607,Chi2Text);
    texf->Draw();

    ctmp->SetLogy();
    ctmp->SaveAs(TString::Format("plots/FitBackground_cat%d.png",c));
    ctmp->SaveAs(TString::Format("plots/FitBackground_cat%d.root",c));

    delete ctmp;    

    //********************************************************************************//

    /*    
    if (dobands) {

      RooAbsPdf *cpdf; cpdf = MggBkgTmp0;
      TGraphAsymmErrors *onesigma = new TGraphAsymmErrors();
      TGraphAsymmErrors *twosigma = new TGraphAsymmErrors();
      
      RooRealVar *nlim = new RooRealVar(TString::Format("nlim%d",c),"",0.0,0.0,10.0);
      nlim->removeRange();
      
      RooCurve *nomcurve = dynamic_cast<RooCurve*>(plotMggBkg[c]->getObject(1));
      
      for (int i=1; i<(plotMggBkg[c]->GetXaxis()->GetNbins()+1); ++i) {
	double lowedge = plotMggBkg[c]->GetXaxis()->GetBinLowEdge(i);
	double upedge  = plotMggBkg[c]->GetXaxis()->GetBinUpEdge(i);
	double center  = plotMggBkg[c]->GetXaxis()->GetBinCenter(i);
	
	double nombkg = nomcurve->interpolate(center);
	nlim->setVal(nombkg);
	mgg->setRange("errRange",lowedge,upedge);
	RooAbsPdf *epdf = 0;
	epdf = new RooExtendPdf("epdf","",*cpdf,*nlim,"errRange");
	
	RooAbsReal *nll = epdf->createNLL(*(data[c]),Extended());
	RooMinimizer minim(*nll);
	minim.setStrategy(0);
	double clone = 1.0 - 2.0*RooStats::SignificanceToPValue(1.0);
	double cltwo = 1.0 - 2.0*RooStats::SignificanceToPValue(2.0);
	
	minim.migrad();
	minim.minos(*nlim);
	// printf("errlo = %5f, errhi = %5f\n",nlim->getErrorLo(),nlim->getErrorHi());
	
	onesigma->SetPoint(i-1,center,nombkg);
	onesigma->SetPointError(i-1,0.,0.,-nlim->getErrorLo(),nlim->getErrorHi());
	
	minim.setErrorLevel(0.5*pow(ROOT::Math::normal_quantile(1-0.5*(1-cltwo),1.0), 2)); // the 0.5 is because qmu is -2*NLL
	// eventually if cl = 0.95 this is the usual 1.92!      
	
	
	minim.migrad();
	minim.minos(*nlim);
	
	twosigma->SetPoint(i-1,center,nombkg);
	twosigma->SetPointError(i-1,0.,0.,-nlim->getErrorLo(),nlim->getErrorHi());
	
	
	delete nll;
	delete epdf;
	
      }
      mgg->setRange("errRange",minMassFit,maxMassFit);
      
      twosigma->SetLineColor(kGreen);
      twosigma->SetFillColor(kGreen);
      twosigma->SetMarkerColor(kGreen);
      twosigma->Draw("L3 SAME");
      
      onesigma->SetLineColor(kYellow);
      onesigma->SetFillColor(kYellow);
      onesigma->SetMarkerColor(kYellow);
      onesigma->Draw("L3 SAME");
      
      plotMggBkg[c]->Draw("SAME"); 
     
    }//end dobands if-statement
    */     

  }//end loop over categories
  
  return fitresult;

}


void SetConstantParams(const RooArgSet* params) {

  TIterator* iter(params->createIterator());
  for (TObject *a = iter->Next(); a != 0; a = iter->Next()) {
    RooRealVar *rrv = dynamic_cast<RooRealVar *>(a);
    if (rrv) { rrv->setConstant(true); std::cout << " " << rrv->GetName(); }
  }  

}

void MakePlots(RooWorkspace* w, Float_t mass, RooFitResult* fitresults, bool isWW) {

  cout << "Start plotting" << endl; 
  
  Int_t ncat = NCAT;

  std::vector<TString> catdesc;
  catdesc.push_back("#scale[0.8]{WW_mass_ele_HP}");
  catdesc.push_back("#scale[0.8]{WW_mass_ele_LP}");
  catdesc.push_back("#scale[0.8]{WW_mass_mu_HP}");
  catdesc.push_back("#scale[0.8]{WW_mass_mu_LP}");
  
// retrieve data sets from the workspace
  RooDataSet* dataAll         = (RooDataSet*) w->data("Data");
  RooDataSet* signalAll       = (RooDataSet*) w->data("Sig");

  RooDataSet* data[9];  
  RooDataSet* signal[9];
  RooAbsPdf*  MggGaussSig[9];
  RooAbsPdf*  MggCBSig[9];
  RooAbsPdf*  MggSig[9];
  RooAbsPdf*  MggBkg[9];  
//  RooAbsPdf*  MggBkg2[9];  

  for (int c = 0; c < ncat; ++c) {
    data[c]         = (RooDataSet*) w->data(TString::Format("Data_cat%d",c));
//    signal[c]       = (RooDataSet*) w->data(TString::Format("Sig_cat%d",c));
    signal[c]       = (RooDataSet*) w->data(TString::Format("SigWeight_cat%d",c));
    MggGaussSig[c]  = (RooAbsPdf*)  w->pdf(TString::Format("MggGaussSig_cat%d",c));
    MggCBSig[c]     = (RooAbsPdf*)  w->pdf(TString::Format("MggCBSig_cat%d",c));
    MggSig[c]       = (RooAbsPdf*)  w->pdf(TString::Format("MggSig_cat%d",c));
    MggBkg[c]       = (RooAbsPdf*)  w->pdf(TString::Format("MggBkg_cat%d",c));
//    MggBkg2[c]      = (RooAbsPdf*)  w->pdf(TString::Format("MggBkg2_cat%d",c));
  }

// retrieve mass observable from the workspace
  RooRealVar* mgg     = w->var("mZZ");  
  mgg->setUnit("GeV");

// retrieve pdfs after the fits
// Signal Model

  RooAbsPdf* MggGaussSigAll  = w->pdf("MggGaussSig");
  RooAbsPdf* MggCBSigAll     = w->pdf("MggCBSig");
  RooAbsPdf* MggSigAll       = w->pdf("MggSig");

//  RooAbsPdf* MggBkgAll       = w->pdf("MggBkg");
  RooAbsPdf* MggBkgAll       = w->pdf("MggBkgAll");
  
  cout << "Progress plotting" << endl;
 
  //****************************//
  // Plot Mgg Fit results
  //****************************//
  // Set P.D.F. parameter names
  // WARNING: Do not use it if Workspaces are created
  //  SetParamNames(w);
  
  
  Float_t minMassFit(MMIN),maxMassFit(MMAX); 
  Float_t MASS(mass);

  Int_t nBinsMass(50);
  
  RooPlot* plotMggAll = mgg->frame(Range(minMassFit,maxMassFit),Bins(nBinsMass));
  signalAll->plotOn(plotMggAll);
 
  gStyle->SetOptTitle(0);
  MggSigAll->plotOn(plotMggAll);
  MggSigAll->plotOn(plotMggAll,Components("MggGaussSig"),LineStyle(kDashed),LineColor(kGreen));
  MggSigAll->plotOn(plotMggAll,Components("MggCBSig"),LineStyle(kDashed),LineColor(kRed));

  MggSigAll->paramOn(plotMggAll, ShowConstants(true), Layout(0.15,0.55,0.9), Format("NEU",AutoPrecision(2)));
  plotMggAll->getAttText()->SetTextSize(0.03);

  TCanvas* c1 = new TCanvas("c1","M(VV)",0,0,500,500);
  c1->cd(1);
  plotMggAll->Draw();  


  cout << "Progress plotting" << endl;

//********************************************//
// Plot Mgg signal fit results per categories 
//********************************************//
// Plot Signal Categories 
//****************************//

  TLatex *text = new TLatex();
  text->SetNDC();
  text->SetTextSize(0.04);

//  TCanvas* c2 = new TCanvas("c2","Mgg Categories",0,0,1000,1000);

//  c2->Divide(3,3);
  RooPlot* plotMgg[9];
  for (int c = 0; c < ncat; ++c) {
    plotMgg[c] = mgg->frame(Range(minMassFit,maxMassFit),Bins(nBinsMass));
    signal[c]->plotOn(plotMgg[c],LineColor(kWhite),MarkerColor(kWhite));    

    MggSig[c]  ->plotOn(plotMgg[c]);
    MggSig[c]  ->plotOn(plotMgg[c],Components(TString::Format("MggGaussSig_cat%d",c)),LineStyle(kDashed),LineColor(kGreen));
    MggSig[c]  ->plotOn(plotMgg[c],Components(TString::Format("MggCBSig_cat%d",c)),LineStyle(kDashed),LineColor(kRed));
    

    MggSig[c]  ->paramOn(plotMgg[c]);
    signal[c]  ->plotOn(plotMgg[c]);

        
    TCanvas* dummy = new TCanvas("dummy", "dummy",0, 0, 400, 400);
    TH1F *hist = new TH1F("hist", "hist", 400, minMassFit, maxMassFit);
 
    plotMgg[c]->SetTitle("");      
    plotMgg[c]->SetMinimum(0.0);
    plotMgg[c]->SetMaximum(1.40*plotMgg[c]->GetMaximum());
    plotMgg[c]->GetXaxis()->SetTitle("m_{#gamma#gamma} (GeV)");

    TCanvas* ctmp = new TCanvas("ctmp","M(VV) Background Categories",0,0,500,500);
    plotMgg[c]->Draw();  
//    hist->Draw("same");
    
    plotMgg[c]->Draw("SAME");  
    TLegend *legmc = new TLegend(0.62,0.75,0.92,0.9);
    legmc->AddEntry(plotMgg[c]->getObject(5),"Simulation","LPE");
    legmc->AddEntry(plotMgg[c]->getObject(1),"Parametric Model","L");
    legmc->AddEntry(plotMgg[c]->getObject(3),"Crystal Ball component","L");
    legmc->AddEntry(plotMgg[c]->getObject(2),"Gaussian Outliers","L");
    
    legmc->SetBorderSize(0);
    legmc->SetFillStyle(0);
    legmc->Draw();    
    
    float effS = effSigma(hist);
//    text->DrawLatex(0.65,0.4, TString::Format("#sigma_{eff} = %.2f GeV",effS));
//    cout<<"effective sigma [" << c << "] = " << effS <<endl;
    
    TLatex *lat  = new TLatex(minMassFit+1.5,0.85*plotMgg[c]->GetMaximum(),"#scale[1.0]{CMS Preliminary}");
    lat->Draw();
    TLatex *lat2 = new TLatex(minMassFit+1.5,0.75*plotMgg[c]->GetMaximum(),catdesc.at(c));
    lat2->Draw();
    TLatex *lat3 = new TLatex(minMassFit+1.5,0.55*plotMgg[c]->GetMaximum(),TString::Format("#scale[0.8]{#sigma_{eff} = %.2f GeV}",effS));
    lat3->Draw();

    int iMass = abs(mass);

    if (!isWW){
      ctmp->SaveAs(TString::Format("plots/sigmodel_ZZ%d_cat%d.png", iMass, c));
      ctmp->SaveAs(TString::Format("plots/sigmodel_ZZ%d_cat%d.pdf", iMass, c));
      ctmp->SaveAs(TString::Format("plots/sigmodel_ZZ%d_cat%d.eps", iMass, c));
      ctmp->SaveAs(TString::Format("plots/sigmodel_ZZ%d_cat%d.C", iMass, c));
    } else {
      ctmp->SaveAs(TString::Format("plots/sigmodel_WW%d_cat%d.png", iMass, c));
      ctmp->SaveAs(TString::Format("plots/sigmodel_WW%d_cat%d.pdf", iMass, c));
      ctmp->SaveAs(TString::Format("plots/sigmodel_WW%d_cat%d.eps", iMass, c));
      ctmp->SaveAs(TString::Format("plots/sigmodel_WW%d_cat%d.C", iMass, c));
    }


  }


//****************************//
// Plot Mgg Background 
//****************************//
/*
  nBinsMass=80;
  RooPlot* plotMggBkgAll = mgg->frame(nBinsMass);
  dataAll->plotOn(plotMggBkgAll,LineColor(kWhite),MarkerColor(kWhite)); 
  fitresults->Print();

  MggBkgAll->plotOn(plotMggBkgAll,FillColor(kYellow),Range("fitrange"),NormRange("fitrange"), VisualizeError(*fitresults, 2.0,kFALSE));
  MggBkgAll->plotOn(plotMggBkgAll,FillColor(kGreen),Range("fitrange"),NormRange("fitrange"), VisualizeError(*fitresults, 1.0,kFALSE));
  MggBkgAll->plotOn(plotMggBkgAll,LineColor(kBlue),Range("fitrange"),NormRange("fitrange"));
  MggBkgAll->plotOn(plotMggBkgAll,Components("MggBkgAll2"),LineStyle(kDashed),LineColor(kRed));
  dataAll->plotOn(plotMggBkgAll); 
//  MggBkgAll->paramOn(plotMggBkgAll, ShowConstants(true), Layout(0.65,0.9,0.9), Format("NEU",AutoPrecision(4)));
//  plotMggBkgAll->getAttText()->SetTextSize(0.03);



  TCanvas* c3 = new TCanvas("c3","Mgg Background",0,0,500,500);
  plotMggBkgAll->Draw();  
  TLegend *legmc = new TLegend(0.62,0.75,0.92,0.9);
  legmc->AddEntry(plotMggBkgAll->getObject(4),"Data (5.3/fb)","LPE");
  legmc->AddEntry(plotMggBkgAll->getObject(3),"Bkg Model","L");
  legmc->AddEntry(plotMggBkgAll->getObject(2),"#pm1 #sigma","F");
  legmc->AddEntry(plotMggBkgAll->getObject(1),"#pm2 #sigma","F");
  legmc->SetBorderSize(0);
  legmc->SetFillStyle(0);
  legmc->Draw();

  text->DrawLatex(0.2,0.85,"CMS Preliminary");
  text->DrawLatex(0.2,0.78,"#sqrt{s} = 8 TeV L =5.3 fb^{-1}");

*/
//************************************************//
// Plot Mgg background fit results per categories 
//************************************************//
// Plot Background Categories 
//****************************//

  TCanvas* c4 = new TCanvas("c4","M(VV) Background Categories",0,0,1000,1000);
  c4->Divide(2,3);

  RooPlot* plotMggBkg[9];
  for (int c = 0; c < ncat; ++c) {
    plotMggBkg[c] = mgg->frame(nBinsMass);
    data[c]->plotOn(plotMggBkg[c],LineColor(kWhite),MarkerColor(kWhite));    
    MggBkg[c]->plotOn(plotMggBkg[c],LineColor(kBlue),Range("fitrange"),NormRange("fitrange")); 
    data[c]->plotOn(plotMggBkg[c]);    
    MggBkg[c]->paramOn(plotMggBkg[c], ShowConstants(true), Layout(0.65,0.9,0.9), Format("NEU",AutoPrecision(4)));
    plotMggBkg[c]->getAttText()->SetTextSize(0.03);
    c4->cd(c+1);
    plotMggBkg[c]->Draw();  
    gPad->SetLogy(1);
  }

  c4->SaveAs(TString::Format("plots/backgrounds_log.png",c));
  c4->SaveAs(TString::Format("plots/backgrounds_log.pdf",c));
  c4->SaveAs(TString::Format("plots/backgrounds_log.eps",c));
  c4->SaveAs(TString::Format("plots/backgrounds_log.C",c));



  TCanvas* c5 = new TCanvas("c5","M(VV) Background Categories",0,0,1000,1000);
  c5->Divide(2,3);

  RooPlot* plotMggBkg[9];
  for (int c = 0; c < ncat; ++c) {
    plotMggBkg[c] = mgg->frame(nBinsMass);
    data[c]->plotOn(plotMggBkg[c],LineColor(kWhite),MarkerColor(kWhite));    
    MggBkg[c]->plotOn(plotMggBkg[c],LineColor(kBlue),Range("fitrange"),NormRange("fitrange")); 
    data[c]->plotOn(plotMggBkg[c]);    
    MggBkg[c]->paramOn(plotMggBkg[c], ShowConstants(true), Layout(0.65,0.9,0.9), Format("NEU",AutoPrecision(4)));
    plotMggBkg[c]->getAttText()->SetTextSize(0.03);
    c5->cd(c+1);
    plotMggBkg[c]->Draw();  
  }

  c5->SaveAs(TString::Format("plots/backgrounds.png",c));
  c5->SaveAs(TString::Format("plots/backgrounds.pdf",c));
  c5->SaveAs(TString::Format("plots/backgrounds.eps",c));
  c5->SaveAs(TString::Format("plots/backgrounds.C",c));

}


void SetParamNames(RooWorkspace* w) {
  
  Int_t ncat = NCAT;

//****************************//
// Mgg signal all categories
//****************************//

  RooRealVar* mgg_sig_m0     = w->var("mgg_sig_m0");  
  RooRealVar* mgg_sig_sigma  = w->var("mgg_sig_sigma");
  RooRealVar* mgg_sig_alpha  = w->var("mgg_sig_alpha"); 
  RooRealVar* mgg_sig_n      = w->var("mgg_sig_n"); 
  RooRealVar* mgg_sig_gsigma = w->var("mgg_sig_gsigma");
  RooRealVar* mgg_sig_frac   = w->var("mgg_sig_frac");

  mgg_sig_m0    ->SetName("m_{0}");
  mgg_sig_sigma ->SetName("#sigma_{CB}");
  mgg_sig_alpha ->SetName("#alpha");
  mgg_sig_n     ->SetName("n");
  mgg_sig_gsigma->SetName("#sigma_G");  
  mgg_sig_frac  ->SetName("f_G");  

  mgg_sig_m0    ->setUnit("GeV");
  mgg_sig_sigma ->setUnit("GeV");
  mgg_sig_gsigma->setUnit("GeV"); 

//****************************//
// Mgg background  
//****************************//

  RooRealVar* mgg_bkg_8TeV_slope1  = w->var("mgg_bkg_8TeV_slope1");
  mgg_bkg_8TeV_slope1              ->SetName("a_{B}");
  mgg_bkg_8TeV_slope1              ->setUnit("1/GeV");

  RooRealVar* mgg_bkg_8TeV_slope2  = w->var("mgg_bkg_8TeV_slope2");
  mgg_bkg_8TeV_slope2              ->SetName("a_{B}");
  mgg_bkg_8TeV_slope2              ->setUnit("1/GeV");



//****************************//
// Mgg per category  
//****************************//

  for (int c = 0; c < ncat; ++c) {


    mgg_sig_m0     = (RooRealVar*) w->var(TString::Format("mgg_sig_m0_cat%d",c));
    mgg_sig_sigma  = (RooRealVar*) w->var(TString::Format("mgg_sig_sigma_cat%d",c));
    mgg_sig_alpha  = (RooRealVar*) w->var(TString::Format("mgg_sig_alpha_cat%d",c));
    mgg_sig_n      = (RooRealVar*) w->var(TString::Format("mgg_sig_n_cat%d",c));
    mgg_sig_gsigma = (RooRealVar*) w->var(TString::Format("mgg_sig_gsigma_cat%d",c));
    mgg_sig_frac   = (RooRealVar*) w->var(TString::Format("mgg_sig_frac_cat%d",c));

    mgg_sig_m0     ->SetName("m_{0}"); 
    mgg_sig_sigma  ->SetName("#sigma_{CB}");
    mgg_sig_alpha  ->SetName("#alpha");
    mgg_sig_n      ->SetName("n"); 
    mgg_sig_gsigma ->SetName("#sigma_{G}");
    mgg_sig_frac   ->SetName("f_{G}");


    mgg_sig_m0     ->setUnit("GeV");
    mgg_sig_sigma  ->setUnit("GeV");
    mgg_sig_gsigma ->setUnit("GeV");


    mgg_bkg_8TeV_slope1 = w->var(TString::Format("mgg_bkg_8TeV_slope1_cat%d",c));
    mgg_bkg_8TeV_slope1 ->SetName("p_{B}^{1}");
    mgg_bkg_8TeV_slope1 ->setUnit("1/GeV");

    mgg_bkg_8TeV_slope2 = w->var(TString::Format("mgg_bkg_8TeV_slope2_cat%d",c));
    mgg_bkg_8TeV_slope2 ->SetName("p_{B}^{2}");
    mgg_bkg_8TeV_slope2 ->setUnit("1/GeV^{2}");

//    RooRealVar* mgg_bkg_8TeV_frac = w->var(TString::Format("mgg_bkg_8TeV_frac_cat%d",c));
//    mgg_bkg_8TeV_frac ->SetName("f");

  }

}



void MakeSigWS(RooWorkspace* w, const char* fileBaseName) {

  TString wsDir   = "workspaces/";
  Int_t ncat = NCAT;

  //**********************************************************************//
  // Write pdfs and datasets into the workspace 
  // for statistical tests. 
  // 0 ele_LP
  // 1 ele_HP
  // 2 mu_LP
  // 3 mu_HP
  //**********************************************************************//

  //********************************//
  // Retrieve P.D.F.s
  //********************************//

  RooAbsPdf* MggSigPdf[4];
  
  // (1) import signal P.D.F.s

  RooWorkspace *wAll = new RooWorkspace("w_all","w_all");


  for (int c = 0; c < ncat; ++c) {
    MggSigPdf[c] = (RooAbsPdf*)  w->pdf(TString::Format("MggSig_cat%d",c)); //actually, not used...
    wAll->import(*w->pdf(TString::Format("MggSig_cat%d",c)));
  }

  // (2) Systematics on energy scale and resolution

  wAll->factory("CMS_hgg_sig_m0_absShift[1,0.5,1.5]");

  //multiply by scale factor
  wAll->factory("prod::CMS_hgg_sig_m0_cat0(mgg_sig_m0_cat0, CMS_hgg_sig_m0_absShift)");
  wAll->factory("prod::CMS_hgg_sig_m0_cat1(mgg_sig_m0_cat1, CMS_hgg_sig_m0_absShift)");
  wAll->factory("prod::CMS_hgg_sig_m0_cat2(mgg_sig_m0_cat2, CMS_hgg_sig_m0_absShift)");
  wAll->factory("prod::CMS_hgg_sig_m0_cat3(mgg_sig_m0_cat3, CMS_hgg_sig_m0_absShift)");

  // (3) Systematics on resolution: create new sigmas
  
  wAll->factory("CMS_hgg_sig_sigmaScale[1,0.5,1.5]");

  //multiply by scale factor
  wAll->factory("prod::CMS_hgg_sig_sigma_cat0(mgg_sig_sigma_cat0, CMS_hgg_sig_sigmaScale)");
  wAll->factory("prod::CMS_hgg_sig_sigma_cat1(mgg_sig_sigma_cat1, CMS_hgg_sig_sigmaScale)");
  wAll->factory("prod::CMS_hgg_sig_sigma_cat2(mgg_sig_sigma_cat2, CMS_hgg_sig_sigmaScale)");
  wAll->factory("prod::CMS_hgg_sig_sigma_cat3(mgg_sig_sigma_cat3, CMS_hgg_sig_sigmaScale)");

  // (4) do reparametrization of signal
  for (int c = 0; c < ncat; ++c) {
    wAll->factory(
		  TString::Format("EDIT::CMS_hgg_sig_cat%d(MggSig_cat%d,",c,c) +
		  TString::Format(" mgg_sig_m0_cat%d=CMS_hgg_sig_m0_cat%d, ", c,c) +
		  TString::Format(" mgg_sig_sigma_cat%d=CMS_hgg_sig_sigma_cat%d) ", c,c)
		  );
  }

  TString filename(wsDir+TString(fileBaseName)+".inputsig.root");
  wAll->writeToFile(filename);
  cout << "Write signal workspace in: " << filename << " file" << endl;

  return;
}


void MakeBkgWS(RooWorkspace* w, const char* fileBaseName) {

  TString wsDir   = "workspaces/";
  Int_t ncat = NCAT;  

  //**********************************************************************//
  // Write pdfs and datasets into the workspace 
  // for statistical tests. 
  // 
  // Suffix to attribute belonging to given the category
  // "catN"    - N shower shape, pseudo-rapidity, pt or Njets categories 
  //  N=0-3    - default shower shape, pseudo-rapidity 4 categories
  //  N=0-3    - Pt<40 GeV or 0-jet (Central Jet Veto)
  //  N=4-7    - Pt>40 GeV or 1-jet (one-jet tagging)
  //**********************************************************************//

  //********************************//
  // Retrieve the datasets and PDFs
  //********************************//

  RooDataSet* data[NCAT];
  RooExtendPdf* MggBkgPdf[NCAT];

  // (1) import everything

  cout << "Start importing everything for data" << endl;

  RooWorkspace *wAll = new RooWorkspace("w_all","w_all");

  for (int c = 0; c < ncat; ++c) {
 
    cout << "For category " << c << endl;

    data[c]      = (RooDataSet*) w->data(TString::Format("Data_cat%d",c));
    //binning the dataset (1 GeV) --> why not unbinned?
    ((RooRealVar*) data[c]->get()->find("mZZ"))->setBins(MMAX-MMIN) ;
    RooDataHist* dataBinned = data[c]->binnedClone();

    MggBkgPdf[c] = (RooExtendPdf*)  w->pdf(TString::Format("MggBkg_cat%d",c)); //actually, not used...
    //   wAll->import(*data[c], Rename(TString::Format("data_obs_cat%d",c))); // unbinned 
    wAll->import(*dataBinned, Rename(TString::Format("data_obs_cat%d",c)));   // binned
    wAll->import(*w->pdf(TString::Format("MggBkg_cat%d",c)));

    //NOTE: Check the ranges in the file : Xvv_models_Bkg_8TeV_test.rs
    double mean = wAll->var(TString::Format("mgg_bkg_8TeV_norm_cat%d",c))->getVal();
    double min = wAll->var(TString::Format("mgg_bkg_8TeV_norm_cat%d",c))->getMin();
    double max = wAll->var(TString::Format("mgg_bkg_8TeV_norm_cat%d",c))->getMax();
    wAll->factory(TString::Format("CMS_hgg_bkg_8TeV_cat%d_norm[%g,%g,%g]", c, mean, min, max));

    // From pure ROOT: should be around 100.0
    mean = wAll->var(TString::Format("mgg_bkg_8TeV_slope1_cat%d",c))->getVal();
    min = wAll->var(TString::Format("mgg_bkg_8TeV_slope1_cat%d",c))->getMin();
    max = wAll->var(TString::Format("mgg_bkg_8TeV_slope1_cat%d",c))->getMax();
    wAll->factory(TString::Format("CMS_hgg_bkg_8TeV_slope1_cat%d[%g,%g,%g]", c, mean, min, max));

    // From pure ROOT: should be around 0.05
    mean = wAll->var(TString::Format("mgg_bkg_8TeV_slope2_cat%d",c))->getVal();
    min = wAll->var(TString::Format("mgg_bkg_8TeV_slope2_cat%d",c))->getMin();
    max = wAll->var(TString::Format("mgg_bkg_8TeV_slope2_cat%d",c))->getMax();
    wAll->factory(TString::Format("CMS_hgg_bkg_8TeV_slope2_cat%d[%g,%g,%g]", c, mean, min, max));

    mean = wAll->var(TString::Format("mgg_bkg_8TeV_slope3_cat%d",c))->getVal();
    min = wAll->var(TString::Format("mgg_bkg_8TeV_slope3_cat%d",c))->getMin();
    max = wAll->var(TString::Format("mgg_bkg_8TeV_slope3_cat%d",c))->getMax();
    wAll->factory(TString::Format("CMS_hgg_bkg_8TeV_slope3_cat%d[%g,%g,%g]", c, mean, mean, mean)); //P3 fixed
    //wAll->factory(TString::Format("CMS_hgg_bkg_8TeV_slope3_cat%d[%g,%g,%g]", c, mean, min, max)); //P3 floating
    //If you change this part you have to change also this line above:
    // ((RooRealVar*) w->var(TString::Format("mgg_bkg_8TeV_slope3_cat%d",c)))->setConstant(true);

    cout << "Done For category " << c << endl;    
  }
  
  cout << "Imported" << endl;

  // (2) do reparametrization of background

  for (int c = 0; c < ncat; ++c) {
    wAll->factory(
		  TString::Format("EDIT::CMS_hgg_bkg_8TeV_cat%d(MggBkg_cat%d,",c,c) +
		  TString::Format(" mgg_bkg_8TeV_norm_cat%d=CMS_hgg_bkg_8TeV_cat%d_norm,", c,c)+
		  TString::Format(" mgg_bkg_8TeV_slope1_cat%d=CMS_hgg_bkg_8TeV_slope1_cat%d,", c,c)+
		  TString::Format(" mgg_bkg_8TeV_slope2_cat%d=CMS_hgg_bkg_8TeV_slope2_cat%d,", c,c)+
		  TString::Format(" mgg_bkg_8TeV_slope3_cat%d=CMS_hgg_bkg_8TeV_slope3_cat%d)", c,c)
		  );
  } 


  TString filename(wsDir+TString(fileBaseName)+".root");
  wAll->writeToFile(filename);
  cout << "Write background workspace in: " << filename << " file" << endl;

  cout << endl;
  std::cout << "observation " << endl;
  for (int c = 0; c < ncat; ++c) {
    std::cout << "  " << wAll->data(TString::Format("data_obs_cat%d",c))->sumEntries() << endl;
    wAll->data(TString::Format("data_obs_cat%d",c))->Print();
    cout << endl;
  }
  std::cout << std::endl;
  
  //## Check that what we write makes sense?
  for (int c = 0; c < ncat; ++c) {
    cout << endl;
    printf("CMS_hgg_bkg_8TeV_slope1_cat%d  param  %.4f  # Mean of background slope\n",
   	   c, wAll->var(TString::Format("CMS_hgg_bkg_8TeV_slope1_cat%d",c))->getVal());
    printf("CMS_hgg_bkg_8TeV_slope2_cat%d  param  %.4f  # Mean of background slope\n",
   	   c, wAll->var(TString::Format("CMS_hgg_bkg_8TeV_slope2_cat%d",c))->getVal());
    printf("CMS_hgg_bkg_8TeV_slope3_cat%d  param  %.4f  # Mean of background slope\n",
   	   c, wAll->var(TString::Format("CMS_hgg_bkg_8TeV_slope3_cat%d",c))->getVal());
  }

  return;
}

Double_t effSigma(TH1 *hist) {

  TAxis *xaxis = hist->GetXaxis();
  Int_t nb = xaxis->GetNbins();
  if(nb < 10) {
    std::cout << "effsigma: Not a valid histo. nbins = " << nb << std::endl;
    return 0.;
  }

  Double_t bwid = xaxis->GetBinWidth(1);
  if(bwid == 0) {
    std::cout << "effsigma: Not a valid histo. bwid = " << bwid << std::endl;
    return 0.;
  }
  Double_t xmax = xaxis->GetXmax();
  Double_t xmin = xaxis->GetXmin();
  Double_t ave = hist->GetMean();
  Double_t rms = hist->GetRMS();

  Double_t total=0.;
  for(Int_t i=0; i<nb+2; i++) {
    total+=hist->GetBinContent(i);
  }
  if(total < 100.) {
    std::cout << "effsigma: Too few entries " << total << std::endl;
    return 0.;
  }
  Int_t ierr=0;
  Int_t ismin=999;

  Double_t rlim=0.683*total;
  Int_t nrms=rms/(bwid);    // Set scan size to +/- rms
  if(nrms > nb/10) nrms=nb/10; // Could be tuned...

  Double_t widmin=9999999.;
  for(Int_t iscan=-nrms;iscan<nrms+1;iscan++) { // Scan window centre
    Int_t ibm=(ave-xmin)/bwid+1+iscan;
    Double_t x=(ibm-0.5)*bwid+xmin;
    Double_t xj=x;
    Double_t xk=x;
    Int_t jbm=ibm;
    Int_t kbm=ibm;
    Double_t bin=hist->GetBinContent(ibm);
    total=bin;
    for(Int_t j=1;j<nb;j++){
      if(jbm < nb) {
        jbm++;
        xj+=bwid;
        bin=hist->GetBinContent(jbm);
        total+=bin;
        if(total > rlim) break;
      }
      else ierr=1;
      if(kbm > 0) {
        kbm--;
        xk-=bwid;
        bin=hist->GetBinContent(kbm);
        total+=bin;
        if(total > rlim) break;
      }
      else ierr=1;
    }
    Double_t dxf=(total-rlim)*bwid/bin;
    Double_t wid=(xj-xk+bwid-dxf)*0.5;
    if(wid < widmin) {
      widmin=wid;
      ismin=iscan;
    }
  }
  if(ismin == nrms || ismin == -nrms) ierr=3;
  if(ierr != 0) std::cout << "effsigma: Error of type " << ierr << std::endl;

  return widmin;
}



void MakeDataCard_1Channel(RooWorkspace* w, const char* fileBaseName, const char* fileBkgName, int iChan, float mass) {

  double ScaleFactorSignal = 1.;
  //double ScaleFactorSignal = 500.; // Such that we expect ~10 events for Bulk Graviton, M=2 TeV, c=0.2

  TString cardDir = TString::Format("datacards/%d/",int(mass));
  Int_t ncat = NCAT;
  TString wsDir   = "../workspaces/";

  //   //Create directory for each mass point

  //   sprintf(thisMassPointDir,"datacards/%d",int(mass)); 
  //   cout << "Creating directory: " << thisMassPointDir << endl;
  //   System("mkdir pippo");

  //**********************//
  // Retrieve the datasets
  //**********************//

  cout << "Start retrieving dataset" << endl;

  RooDataSet* data[NCAT];
  RooDataSet* signal[NCAT];
  for (int c = 0; c < ncat; ++c) {
    data[c]        = (RooDataSet*) w->data(TString::Format("Data_cat%d",c));
    signal[c]      = (RooDataSet*) w->data(TString::Format("SigWeight_cat%d",c));
  }

  RooRealVar*  lumi = w->var("lumi");

  //*****************************//
  // Print Expected event yields
  //*****************************//

  cout << "======== Expected Events Number =====================" << endl;  
  cout << ".........Measured Data for L = " << lumi->getVal() << " pb-1 ............................" << endl;  
  cout << "#Events data:        " <<  w->data("Data")->sumEntries()  << endl;
  for (int c = 0; c < ncat; ++c) {
    cout << TString::Format("#Events data cat%d:   ",c) << data[c]->sumEntries()  << endl;
  }
  cout << ".........Expected Signal for L = " << lumi->getVal() << " pb-1 ............................" << endl;  
  cout << "#Events Signal:      " << w->data("SigWeight")->sumEntries()  << endl;

  //Float_t siglikeErr[NCAT];
  for (int c = 0; c < ncat; ++c) {
    cout << TString::Format("#Events Signal cat%d: ",c) << signal[c]->sumEntries()*lumi->getVal() << endl;
    //siglikeErr[c]=0.6*signal[c]->sumEntries();
  }
  cout << "====================================================" << endl;  


  //*************************//
  // Print Data Crd int file
  //*************************//


  TString filename(cardDir+TString(fileBaseName)+Form("_channel%d.txt",iChan));
  ofstream outFile(filename);


  outFile << "#CMS-HGG DataCard for Unbinned Limit Setting, " << lumi->getVal() <<  " pb-1 " << endl;
  outFile << "#Run with: combine -d hgg.mH130.0.shapes-Unbinned.txt -U -m 130 -H ProfileLikelihood -M MarkovChainMC --rMin=0 --rMax=20.0  -b 3000 -i 50000 --optimizeSim=1 --tries 30" << endl;
  outFile << "# Lumi =  " << lumi->getVal() << " pb-1" << endl;
  outFile << "imax 1" << endl; // channel or bins
  outFile << "jmax 1" << endl; // backgrounds
  outFile << "kmax *" << endl; // nuisance parameters
  outFile << "---------------" << endl;

  outFile << "shapes *      * " << wsDir+TString(fileBkgName)+".root" << " w_all:$PROCESS_$CHANNEL" << endl;
  outFile << "shapes MggBkg * "<<  wsDir+TString(fileBkgName)+".root" << " w_all:CMS_hgg_bkg_8TeV_$CHANNEL" << endl;
  outFile << "shapes MggSig * " << wsDir+TString(fileBaseName)+".inputsig.root" << " w_all:CMS_hgg_sig_$CHANNEL" << endl;

  outFile << "---------------" << endl;
  outFile << Form("bin          cat%d", iChan) << endl;
  outFile <<  "observation   "  <<  Form("%.10lg",data[iChan]->sumEntries()) << endl;
  outFile << "------------------------------" << endl;
  outFile << "bin                      "<< Form("cat%d       cat%d      ", iChan, iChan) << endl;
  outFile << "process                 MggSig     MggBkg     " << endl;
  outFile << "process                    0          1          " << endl;
  outFile <<  "rate                      " 
	  << "  " << signal[iChan]->sumEntries()*lumi->getVal()*ScaleFactorSignal << "  " << 1 << endl;
  //<< "  " << signal[iChan]->sumEntries()/signal[2]->sumEntries()*20  << "  " << 1 << endl;
  //should we put the correct rate of events?
  outFile << "--------------------------------" << endl;

  //== Uncertainties on SIGNAL NORMALIZATION ==

  // Lumi
  outFile << "lumi_8TeV       lnN  0.956/1.044    - " << endl;

  // Trigger
  outFile <<   "CMS_Trigger_eff_g      lnN    0.99/1.01    - " << endl;
  
  // JES
  double sigmaJES = 0.03; // For ZZ It's 3% flat, right?
  outFile << Form("CMS_JES_eff_g           lnN  %f/%f      - # Signal Efficiency",1-sigmaJES,1+sigmaJES) << endl;

  // W-tag efficiency 
  if(iChan==0 || iChan==2)
    outFile << "CMS_VV_eff_g_LP         lnN  1.10/0.90      - # Signal Efficiency" << endl;
  if(iChan==1 || iChan==3)
    outFile << "CMS_VV_eff_g_HP         lnN  0.90/1.10      - # Signal Efficiency" << endl;
  
  //== Uncertainties on SIGNAL SHAPE ==    

  // JES and JER
  outFile << "# Parametric shape uncertainties, entered by hand." << endl;
  outFile << Form("CMS_hgg_sig_m0_absShift    param   1   0.005   # uncertainty of the mean",iChan) << endl;
  outFile << Form("CMS_hgg_sig_sigmaScale     param   1   0.036   # uncertainty on the sigma",iChan) << endl;
 
  outFile << Form("CMS_hgg_bkg_8TeV_cat%d_norm           flatParam  # Normalization uncertainty on background slope",iChan) << endl;
  outFile << Form("CMS_hgg_bkg_8TeV_slope1_cat%d         flatParam  # Mean and absolute uncertainty on background slope",iChan) << endl;
  outFile << Form("CMS_hgg_bkg_8TeV_slope2_cat%d         flatParam  # Mean and absolute uncertainty on background slope",iChan) << endl;
  outFile << Form("CMS_hgg_bkg_8TeV_slope3_cat%d         flatParam  # Mean and absolute uncertainty on background slope",iChan) << endl;

  outFile.close();

  cout << "Write data card in: " << filename << " file" << endl;

  return;
}


Double_t effSigma(TH1 *hist) {

  TAxis *xaxis = hist->GetXaxis();
  Int_t nb = xaxis->GetNbins();
  if(nb < 10) {
    std::cout << "effsigma: Not a valid histo. nbins = " << nb << std::endl;
    return 0.;
  }

  Double_t bwid = xaxis->GetBinWidth(1);
  if(bwid == 0) {
    std::cout << "effsigma: Not a valid histo. bwid = " << bwid << std::endl;
    return 0.;
  }
  Double_t xmax = xaxis->GetXmax();
  Double_t xmin = xaxis->GetXmin();
  Double_t ave = hist->GetMean();
  Double_t rms = hist->GetRMS();

  Double_t total=0.;
  for(Int_t i=0; i<nb+2; i++) {
    total+=hist->GetBinContent(i);
  }
  if(total < 100.) {
    std::cout << "effsigma: Too few entries " << total << std::endl;
    return 0.;
  }
  Int_t ierr=0;
  Int_t ismin=999;

  Double_t rlim=0.683*total;
  Int_t nrms=rms/(bwid);    // Set scan size to +/- rms
  if(nrms > nb/10) nrms=nb/10; // Could be tuned...

  Double_t widmin=9999999.;
  for(Int_t iscan=-nrms;iscan<nrms+1;iscan++) { // Scan window centre
    Int_t ibm=(ave-xmin)/bwid+1+iscan;
    Double_t x=(ibm-0.5)*bwid+xmin;
    Double_t xj=x;
    Double_t xk=x;
    Int_t jbm=ibm;
    Int_t kbm=ibm;
    Double_t bin=hist->GetBinContent(ibm);
    total=bin;
    for(Int_t j=1;j<nb;j++){
      if(jbm < nb) {
        jbm++;
        xj+=bwid;
        bin=hist->GetBinContent(jbm);
        total+=bin;
        if(total > rlim) break;
      }
      else ierr=1;
      if(kbm > 0) {
        kbm--;
        xk-=bwid;
        bin=hist->GetBinContent(kbm);
        total+=bin;
        if(total > rlim) break;
      }
      else ierr=1;
    }
    Double_t dxf=(total-rlim)*bwid/bin;
    Double_t wid=(xj-xk+bwid-dxf)*0.5;
    if(wid < widmin) {
      widmin=wid;
      ismin=iscan;
    }
  }
  if(ismin == nrms || ismin == -nrms) ierr=3;
  if(ierr != 0) std::cout << "effsigma: Error of type " << ierr << std::endl;

  return widmin;
}

void R2JJFitter(double mass)
{
  // For WW
  //runfits(mass, true);
  // For ZZ
  runfits(mass, false);
}
