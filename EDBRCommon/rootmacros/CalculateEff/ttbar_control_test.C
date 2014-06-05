#include <vector>
#include "TH1.h"
#include "TString.h"
#include "TFile.h"
#include "TTree.h"
#include <iostream>
#include "TCanvas.h"
#include "TStyle.h"

void ttbar_control_test()
{
	TString inputpath = "/afs/cern.ch/work/s/shuai/public/diboson/trees/productionv6/goodbtag/AK7/merged/";
	TString cut = "ttbar_control";
	bool clean = false;
	vector<TString> dataSamples;
	vector<TString> bkgSamples;
	vector<TString> sigSamples;


	dataSamples.push_back("SingleMu_Run2012A_13Jul2012_xww");
	dataSamples.push_back("SingleMu_Run2012A_recover_xww");
	dataSamples.push_back("SingleMu_Run2012B_13Jul2012_xww");
	dataSamples.push_back("SingleMu_Run2012C_24Aug2012_xww");
	dataSamples.push_back("SingleMu_Run2012C_PromptReco_xww");
	dataSamples.push_back("SingleMu_Run2012D_PromptReco_xww");

	bkgSamples.push_back("TTBAR_xww");
	bkgSamples.push_back("WW_xww");
	bkgSamples.push_back("WZ_xww");
	bkgSamples.push_back("ZZ_xww");
	bkgSamples.push_back("WJetsPt50To70_xww");
	bkgSamples.push_back("WJetsPt70To100_xww");
	bkgSamples.push_back("WJetsPt100_xww");
	bkgSamples.push_back("DYJetsPt50To70_xww");
	bkgSamples.push_back("DYJetsPt70To100_xww");
	bkgSamples.push_back("DYJetsPt100_xww");

	sigSamples.push_back("RSG_WW_lvjj_c0p2_M600_xww");
	sigSamples.push_back("RSG_WW_lvjj_c0p2_M1000_xww");
	sigSamples.push_back("RSG_WW_lvjj_c0p2_M1500_xww");
	sigSamples.push_back("BulkG_WW_lvjj_c1p0_M600_xww");
	sigSamples.push_back("BulkG_WW_lvjj_c1p0_M1000_xww");
	sigSamples.push_back("BulkG_WW_lvjj_c1p0_M1500_xww");

	int ndata = dataSamples.size();
	int nbkg  = bkgSamples.size();
	int nsig  = sigSamples.size();

	cout<<"data samples "<<ndata<<"  bkg samples "<<nbkg<<"  signal samples "<<nsig<<endl;	

	TH1F * h1 = new TH1F (cut,cut,ndata+nbkg+nsig,0,ndata+nbkg+nsig);
	h1->GetYaxis()->SetRangeUser(0,1);
	h1->SetBit(TH1::kCanRebin);
	h1->SetStats(0);
	gStyle->SetPaintTextFormat("1.4f");
	//h1->Sumw2();
	TH1F *h2 = (TH1F*)h1->Clone(cut+"_2");
	TH1F *h3 = (TH1F*)h1->Clone(cut+"_3");
	TH1F *h4 = (TH1F*)h1->Clone(cut+"_4");
	TH1F *h5 = (TH1F*)h1->Clone(cut+"_5");
	TH1F *h6 = (TH1F*)h1->Clone(cut+"_6");


	TCanvas * c1 = new TCanvas();	

	for(int i =0; i<ndata+nbkg+nsig; i++   )
	{
		TString filename;
		TString samplename;
		if(i<ndata) 
		{
			filename = "treeEDBR_"+dataSamples.at(i)+".root";
			samplename = dataSamples.at(i);//SingleMu_Run2012A_13Jul2012_xww
			samplename.Remove(samplename.Length()-4,4);//SingleMu_Run2012A_13Jul2012
			samplename.Remove(0,12);//2012A_13Jul2012
		}
		else if(i>=ndata&&i<(ndata+nbkg)) 
		{
			filename = "treeEDBR_"+bkgSamples.at(i-ndata)+".root";
			samplename = bkgSamples.at(i-ndata);//TTBAR_xww
			samplename.Remove(samplename.Length()-4,4);//TTBAR
		}
		else if(i>=(ndata+nbkg)) 
		{
			filename = "treeEDBR_"+sigSamples.at(i-ndata-nbkg)+".root";
			samplename = sigSamples.at(i-ndata-nbkg);//RSG_WW_lvjj_c0p2_M1500_xww,BulkG_WW_lvjj_c1p0_M1500_xww
			samplename.Remove(samplename.Length()-4,4);//RSG_WW_lvjj_c0p2_M1500,BulkG_WW_lvjj_c1p0_M1500
			if(samplename.Contains("RSG"))samplename.Remove(4,8);//RSG_c0p2_M1500
			if(samplename.Contains("BulkG"))samplename.Remove(6,8);//BulkG_c1p0_M1500
		}
		cout<<filename<<endl;
		cout<<samplename<<endl;

		TFile *fp = new TFile(inputpath+"/"+filename);
		TTree * tree = (TTree *) fp->Get("SelectedCandidates");
		int entries = tree->GetEntries();
		cout<<"entries: "<<entries<<endl;

		double pass1=0;
		double pass2=0;
		double pass3=0;
		double pass4=0;
		double pass5=0;
		double pass6=0;
		double total=0;
		int nLooseEle;
		int nLooseMu;
		double nbtagsL[99];
		double nbtagsM[99];
		double nbtagsT[99];
		double nbtagscleanM[99];

		//to make cuts
		double met;
		double ptlep1[99];
		double ptZll[99];
		double ptZjj[99];
		double lep[99];
		int    nCands;
		int    nXjets[99];

		//per event weight
		double PUweight=-1;
		double LumiWeight=-1;
		double GenWeight=-1;


		tree->SetBranchAddress("nLooseMu", &nLooseMu);
		tree->SetBranchAddress("nLooseEle",&nLooseEle); 
		if(clean)
		{
			tree->SetBranchAddress("nbtagscleanL",nbtagsL); 
			tree->SetBranchAddress("nbtagscleanM",nbtagsM); 
			tree->SetBranchAddress("nbtagscleanT",nbtagsT);
		}
		else
		{
			tree->SetBranchAddress("nbtagsL",nbtagsL); 
			tree->SetBranchAddress("nbtagsM",nbtagsM); 
			tree->SetBranchAddress("nbtagsT",nbtagsT);
		}
		tree->SetBranchAddress("nbtagscleanM",nbtagscleanM);
		tree->SetBranchAddress("ptlep1", ptlep1); 
		tree->SetBranchAddress("ptZll", ptZll);
		tree->SetBranchAddress("ptZjj", ptZjj);
		tree->SetBranchAddress("met", &met);
		tree->SetBranchAddress("nXjets", nXjets);
		tree->SetBranchAddress("lep", lep);
		tree->SetBranchAddress("nCands", &nCands);

		tree->SetBranchAddress("PUweight", &PUweight);
		tree->SetBranchAddress("LumiWeight", &LumiWeight);
		tree->SetBranchAddress("GenWeight", &GenWeight);

		bool filled = 0;

		for(int j=0;j<entries;j++)
		{
			tree->GetEntry(j);

			//per event weight
			double actualWeight = PUweight*LumiWeight*GenWeight*19538.85;
			if(i<ndata) actualWeight =1; //for data
			//cout<<actualWeight<<endl;

			filled = 0;
			//if(nCands==0)continue;
			for(int ivec=0;ivec<nCands;ivec++){

				if(filled==0)
				{
					//cout<<nXjets[ivec]<<endl;
					//make cuts
					if((nLooseEle+nLooseMu)!=1)continue;
					if(met<40)continue;
					if(lep[ivec]!=1.)continue;//mu
					if(ptlep1[ivec]<50)continue;
					if(ptZll[ivec]<200)continue;
					if(ptZjj[ivec]<200)continue;
					if(nXjets[ivec]!=1)continue;
					total = total + actualWeight;

					if(nbtagsT[ivec]>=2)pass1=pass1+actualWeight;//TT
					if(nbtagsT[ivec]>=1&&nbtagsM[ivec]>=2)pass2=pass2+actualWeight;//TM--------------------note T is also in M
					if(nbtagsT[ivec]>=1&&nbtagsL[ivec]>=2)pass3=pass3+actualWeight;//TL
					if(nbtagsT[ivec]>=1)pass4=pass4+actualWeight;//T
					if(nbtagsM[ivec]>=1&&nbtagscleanM[ivec]>=1)pass5=pass5+actualWeight;//TM or TT
					if(nbtagsM[ivec]>=1)pass6=pass6+actualWeight;//M

					filled =1;
				}
			}//end of candidates loop

		}//end of tree loop

		double eff1=0;
		double eff2=0;
		double eff3=0;
		double eff4=0;
		double eff5=0;
		double eff6=0;
		if(total!=0)
		{
			eff1 = (double)pass1/(double)total;
			eff2 = (double)pass2/(double)total;
			eff3 = (double)pass3/(double)total;
			eff4 = (double)pass4/(double)total;
			eff5 = (double)pass5/(double)total;
			eff6 = (double)pass6/(double)total;
		}
		cout<<"total: "<<total<<" pass1: "<<pass1<<" eff: "<<eff1<<endl;
		cout<<"total: "<<total<<" pass2: "<<pass2<<" eff: "<<eff2<<endl;
		cout<<"total: "<<total<<" pass3: "<<pass3<<" eff: "<<eff3<<endl;
		cout<<"total: "<<total<<" pass4: "<<pass4<<" eff: "<<eff4<<endl;
		cout<<"total: "<<total<<" pass5: "<<pass5<<" eff: "<<eff5<<endl;
		cout<<"total: "<<total<<" pass6: "<<pass6<<" eff: "<<eff6<<endl;


		h1->Fill(samplename,eff1);	
		h2->Fill(samplename,eff2);	
		h3->Fill(samplename,eff3);	
		h4->Fill(samplename,eff4);	
		h5->Fill(samplename,eff5);	
		h6->Fill(samplename,eff6);


	}//end of sample loop

	c1->SetGridy(1);

	h1->SetTitle(cut+"_TT");
	h1->Draw();
	h1->Draw("TEXT0same");
	c1->SaveAs(cut+"_TT.png");

	h2->SetTitle(cut+"_TM");
	h2->Draw();
	h2->Draw("TEXT0same");
	c1->SaveAs(cut+"_TM.png");

	h3->SetTitle(cut+"_TL");
	h3->Draw();
	h3->Draw("TEXT0same");
	c1->SaveAs(cut+"_TL.png");

	h4->SetTitle(cut+"_T");
	h4->Draw();
	h4->Draw("TEXT0same");
	c1->SaveAs(cut+"_T.png");

	h5->SetTitle(cut+"_MandCM");
	h5->Draw();
	h5->Draw("TEXT0same");
	c1->SaveAs(cut+"_TTorTM.png");

	h6->SetTitle(cut+"M");
	h6->Draw();
	h6->Draw("TEXT0same");
	c1->SaveAs(cut+"_M.png");	


}
