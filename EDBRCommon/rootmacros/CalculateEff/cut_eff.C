#include <vector>
#include "TH1.h"
#include "TString.h"
#include "TFile.h"
#include "TTree.h"
#include <iostream>
#include "TCanvas.h"
#include "TStyle.h"

void cut_eff()
{
	//      TString inputpath = "/afs/cern.ch/work/m/mwang/public/EDBR/trees/productionv1_1130/fullrange/";
	TString inputpath = "/afs/cern.ch/work/m/mwang/public/EDBR/trees/productionv1_0319/fullrange/";
	TString cut = "btag_eff";
	vector<TString> dataSamples;
	vector<TString> bkgSamples;
	vector<TString> sigSamples;
	/*
	   dataSamples.push_back("data_xwh");

	   bkgSamples.push_back("TTBARpowheg_xwh");
	   bkgSamples.push_back("VV_xwh");
	   bkgSamples.push_back("WJetsPt180_xwh");
	   bkgSamples.push_back("DYJets_xwh");
	   bkgSamples.push_back("SingleTop_xwh");

	   sigSamples.push_back("MWp_1000_gg_xwh");
	   sigSamples.push_back("MWp_1500_gg_xwh");
	   sigSamples.push_back("MWp_2000_gg_xwh");
	   sigSamples.push_back("MWp_1000_cc_xwh");
	   sigSamples.push_back("MWp_1500_cc_xwh");
	   sigSamples.push_back("MWp_2000_cc_xwh");
	   sigSamples.push_back("MWp_1000_bb_xwh");
	   sigSamples.push_back("MWp_1500_bb_xwh");
	   sigSamples.push_back("MWp_2000_bb_xwh");

	   sigSamples.push_back("MWp_1000_xwh");
	   sigSamples.push_back("MWp_1500_xwh");
	   sigSamples.push_back("MWp_2000_xwh");
	 */
	dataSamples.push_back("");
	bkgSamples.push_back("TTBARmadgraph_xwh");
	bkgSamples.push_back("WJetsPt180_xwh");
	sigSamples.push_back("MWp_1000_gg_xwh");
	sigSamples.push_back("MWp_1000_cc_xwh");
	sigSamples.push_back("MWp_1000_bb_xwh");
	sigSamples.push_back("MWp_1000_xwh");
	sigSamples.push_back("MWp_1500_gg_xwh");
	sigSamples.push_back("MWp_1500_cc_xwh");
	sigSamples.push_back("MWp_1500_bb_xwh");
	sigSamples.push_back("MWp_1500_xwh");
	sigSamples.push_back("MWp_2000_gg_xwh");
	sigSamples.push_back("MWp_2000_cc_xwh");
	sigSamples.push_back("MWp_2000_bb_xwh");
	sigSamples.push_back("MWp_2000_xwh");


	int ndata = 0;//dataSamples.size();
	int nbkg  = 0; //bkgSamples.size();
	int nsig  = sigSamples.size();

	cout<<"data samples "<<ndata<<"  bkg samples "<<nbkg<<"  signal samples "<<nsig<<endl;

	//TH1F * h1 = new TH1F (cut,cut,ndata+nbkg+nsig+1,0,ndata+nbkg+nsig+1);
	TH1F * h1 = new TH1F (cut,cut,14 ,0,14);// number of samples
	//h1->GetYaxis()->SetRangeUser(0,1);
	h1->SetBit(TH1::kCanRebin);
	h1->SetStats(0);
	gStyle->SetPaintTextFormat("1.4f");
	//h1->Sumw2();
	TH1F *h2 = (TH1F*)h1->Clone(cut+"_2");
	TH1F *h3 = (TH1F*)h1->Clone(cut+"_3");
	TH1F *h4 = (TH1F*)h1->Clone(cut+"_4");
	TH1F *h5 = (TH1F*)h1->Clone(cut+"_5");
	TH1F *h6 = (TH1F*)h1->Clone(cut+"_6");
	TH1F *h7 = (TH1F*)h1->Clone(cut+"_7");
	TH1F *h8 = (TH1F*)h1->Clone(cut+"_8");
	TH1F *h9 = (TH1F*)h1->Clone(cut+"_9");
	TH1F *h10 = (TH1F*)h1->Clone(cut+"_10");
	TH1F *h11 = (TH1F*)h1->Clone(cut+"_11");
	TH1F *h12 = (TH1F*)h1->Clone(cut+"_12");
	TH1F *h13 = (TH1F*)h1->Clone(cut+"_13");
	TH1F *h14 = (TH1F*)h1->Clone(cut+"_14");
	TH1F *h15 = (TH1F*)h1->Clone(cut+"_15");
	/*            TH1F *h16 = (TH1F*)h1->Clone(cut+"_16");
		      TH1F *h17 = (TH1F*)h1->Clone(cut+"_17");
		      TH1F *h18 = (TH1F*)h1->Clone(cut+"_18");
	 */
	TCanvas * c1 = new TCanvas();

	for(int i =0; i<ndata+nbkg+nsig; i++   )
	{
		TString filename;
		TString samplename;
		if(i<ndata)
		{
			filename = "treeEDBR_"+dataSamples.at(i)+".root";
			samplename = dataSamples.at(i);//data_xwh  
			samplename.Remove(samplename.Length()-4,4);//data  
			//samplename.Remove(0,12);//2012A_13Jul2012
		}
		else if(i>=ndata&&i<(ndata+nbkg))
		{
			filename = "treeEDBR_"+bkgSamples.at(i-ndata)+".root";
			samplename = bkgSamples.at(i-ndata);//TTBAR_xwh
			samplename.Remove(samplename.Length()-4,4);//TTBAR
		}
		else if(i>=(ndata+nbkg))
		{
			filename = "treeEDBR_"+sigSamples.at(i-ndata-nbkg)+".root";
			samplename = sigSamples.at(i-ndata-nbkg);//MWp_1000_gg_xwh   //RSG_WW_lvjj_c0p2_M1500_xww,BulkG_WW_lvjj_c1p0_M1500_xww
			samplename.Remove(samplename.Length()-4,4);//MWp_1000_gg     // RSG_WW_lvjj_c0p2_M1500,BulkG_WW_lvjj_c1p0_M1500
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
		double pass7=0;
		double pass8=0;
		double pass9=0;
                double pass10=0;
                double pass11=0;
                double pass12=0;
                double pass13=0;
                double pass14=0;
                double pass15=0;
                double total=0;
		int nLooseEle;
		int nLooseMu;
		float nsubjetbtagL[99];
		float nsubjetbtagM[99];
		float nsubjetbtagT[99];
		float nfatjetbtagL[99];
		float nfatjetbtagM[99];
		float nfatjetbtagT[99];

		//to make cuts
		double met;
		double ptlep1[99];
		double ptZll[99];
		double ptZjj[99];
		double lep[99];
		int    nCands;
		int    nXjets[99];
		double region[99];
                //double mZZ_type2_ptUncorrected[99]; // using mZZ_type2_ptUncorrected, mass window:15%

		// event weight
		double weight=-1;

		tree->SetBranchAddress("nLooseMu", &nLooseMu);
		tree->SetBranchAddress("nLooseEle",&nLooseEle);
		tree->SetBranchAddress("nsubjetbtagL",nsubjetbtagL);
		tree->SetBranchAddress("nsubjetbtagM",nsubjetbtagM);
		tree->SetBranchAddress("nsubjetbtagT",nsubjetbtagT);
		tree->SetBranchAddress("nfatjetbtagL",nfatjetbtagL); 
		tree->SetBranchAddress("nfatjetbtagM",nfatjetbtagM); 
		tree->SetBranchAddress("nfatjetbtagT",nfatjetbtagT);

		tree->SetBranchAddress("ptlep1", ptlep1);
		tree->SetBranchAddress("ptZll", ptZll);
		tree->SetBranchAddress("ptZjj", ptZjj);
		tree->SetBranchAddress("met", &met);
		tree->SetBranchAddress("nXjets", nXjets);
		tree->SetBranchAddress("lep", lep);
		tree->SetBranchAddress("nCands", &nCands);
		tree->SetBranchAddress("region", &region);
                //tree->SetBranchAddress("mZZ_type2_ptUncorrected", &mZZ_type2_ptUncorrected);

		tree->SetBranchAddress("weight", &weight);

		bool filled = 0;

		for(int j=0;j<entries;j++)
		{
			tree->GetEntry(j);

			//per event weight
			double actualWeight = weight*19538.85;
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
					//if(met<80)continue;
					if(lep[ivec]!=1.)continue;//mu
					if(nXjets[ivec]!=1)continue;
					if(region[ivec]!=1)continue;
					total = total + actualWeight;

					if(nsubjetbtagL[ivec]>=0)pass1=pass1+actualWeight;
					if(nsubjetbtagM[ivec]>=0)pass2=pass2+actualWeight;
					if(nsubjetbtagT[ivec]>=0)pass3=pass3+actualWeight;
					if(nsubjetbtagL[ivec]>=1)pass4=pass4+actualWeight;
					if(nsubjetbtagM[ivec]>=1)pass5=pass5+actualWeight;
					if(nsubjetbtagT[ivec]>=1)pass6=pass6+actualWeight;
					if(nsubjetbtagL[ivec]>=2)pass7=pass7+actualWeight;
					if(nsubjetbtagM[ivec]>=2)pass8=pass8+actualWeight;
					if(nsubjetbtagT[ivec]>=2)pass9=pass9+actualWeight;
                                        if(nfatjetbtagL[ivec]>=0)pass10=pass10+actualWeight;
                                        if(nfatjetbtagM[ivec]>=0)pass11=pass11+actualWeight;
                                        if(nfatjetbtagT[ivec]>=0)pass12=pass12+actualWeight;
                                        if(nfatjetbtagL[ivec]>=1)pass13=pass13+actualWeight;
                                        if(nfatjetbtagM[ivec]>=1)pass14=pass14+actualWeight;
                                        if(nfatjetbtagT[ivec]>=1)pass15=pass15+actualWeight;

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
		double eff7=0;
		double eff8=0;
		double eff9=0;
                double eff10=0;
                double eff11=0;
                double eff12=0;
                double eff13=0;
                double eff14=0;
                double eff15=0;
		if(total!=0)
		{
			eff1 = (double)pass1/(double)total;
			eff2 = (double)pass2/(double)total;
			eff3 = (double)pass3/(double)total;
			eff4 = (double)pass4/(double)total;
			eff5 = (double)pass5/(double)total;
			eff6 = (double)pass6/(double)total;
			eff7 = (double)pass7/(double)total;
			eff8 = (double)pass8/(double)total;
			eff9 = (double)pass9/(double)total;
                        eff10 = (double)pass10/(double)total;
                        eff11 = (double)pass11/(double)total;
                        eff12 = (double)pass12/(double)total;
                        eff13 = (double)pass13/(double)total;
                        eff14 = (double)pass14/(double)total;
                        eff15 = (double)pass15/(double)total;
		}
		cout<<"total: "<<total<<" pass1: "<<pass1<<" eff: "<<eff1<<endl;
		cout<<"total: "<<total<<" pass2: "<<pass2<<" eff: "<<eff2<<endl;
		cout<<"total: "<<total<<" pass3: "<<pass3<<" eff: "<<eff3<<endl;
		cout<<"total: "<<total<<" pass4: "<<pass4<<" eff: "<<eff4<<endl;
		cout<<"total: "<<total<<" pass5: "<<pass5<<" eff: "<<eff5<<endl;
		cout<<"total: "<<total<<" pass6: "<<pass6<<" eff: "<<eff6<<endl;
		cout<<"total: "<<total<<" pass7: "<<pass7<<" eff: "<<eff7<<endl;
		cout<<"total: "<<total<<" pass8: "<<pass8<<" eff: "<<eff8<<endl;
		cout<<"total: "<<total<<" pass9: "<<pass9<<" eff: "<<eff9<<endl;
                cout<<"total: "<<total<<" pass10: "<<pass10<<" eff: "<<eff10<<endl;
                cout<<"total: "<<total<<" pass11: "<<pass11<<" eff: "<<eff11<<endl;
                cout<<"total: "<<total<<" pass12: "<<pass12<<" eff: "<<eff12<<endl;
                cout<<"total: "<<total<<" pass13: "<<pass13<<" eff: "<<eff13<<endl;
                cout<<"total: "<<total<<" pass14: "<<pass14<<" eff: "<<eff14<<endl;
                cout<<"total: "<<total<<" pass15: "<<pass15<<" eff: "<<eff15<<endl;

		h1->Fill(samplename,eff1);
		h2->Fill(samplename,eff2);
		h3->Fill(samplename,eff3);
		h4->Fill(samplename,eff4);
		h5->Fill(samplename,eff5);
		h6->Fill(samplename,eff6);
		h7->Fill(samplename,eff7);
		h8->Fill(samplename,eff8);
		h9->Fill(samplename,eff9);
                h10->Fill(samplename,eff10);
                h11->Fill(samplename,eff11);
                h12->Fill(samplename,eff12);
                h13->Fill(samplename,eff13);
                h14->Fill(samplename,eff14);
                h15->Fill(samplename,eff15);
	}//end of sample loop

	c1->SetGridy(1);

	h1->SetTitle(cut+"_nsubjetbtagL0");
	h1->Draw();
	h1->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagL0.png");

	h2->SetTitle(cut+"_nsubjetbtagM0");
	h2->Draw();
	h2->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagM0.png");

	h3->SetTitle(cut+"_nsubjetbtagT0");
	h3->Draw();
	h3->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagT0.png");

	h4->SetTitle(cut+"_nsubjetbtagL1");
	h4->Draw();
	h4->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagL1.png");

	h5->SetTitle(cut+"_nsubjetbtagM1");
	h5->Draw();
	h5->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagM1.png");

	h6->SetTitle(cut+"_nsubjetbtagT1");
	h6->Draw();
	h6->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagT1.png");	

	h7->SetTitle(cut+"_nsubjetbtagL2");
	h7->Draw();
	h7->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagL2.png");

	h8->SetTitle(cut+"_nsubjetbtagM2");
	h8->Draw();
	h8->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagM2.png");

	h9->SetTitle(cut+"_nsubjetbtagT2");
	h9->Draw();
	h9->Draw("TEXT0same");
	c1->SaveAs(cut+"_nsubjetbtagT2.png");

        h10->SetTitle(cut+"_nfatjetbtagL0");
        h10->Draw();
        h10->Draw("TEXT0same");
        c1->SaveAs(cut+"_nfatjetbtagL0.png");

        h11->SetTitle(cut+"_nfatjetbtagM0");
        h11->Draw();
        h11->Draw("TEXT0same");
        c1->SaveAs(cut+"_nfatjetbtagM0.png");

        h12->SetTitle(cut+"_nfatjetbtagT0");
        h12->Draw();
        h12->Draw("TEXT0same");
        c1->SaveAs(cut+"_nfatjetbtagT0.png");

        h13->SetTitle(cut+"_nfatjetbtagL1");
        h13->Draw();
        h13->Draw("TEXT0same");
        c1->SaveAs(cut+"_nfatjetbtagL1.png");

        h14->SetTitle(cut+"_nfatjetbtagM1");
        h14->Draw();
        h14->Draw("TEXT0same");
        c1->SaveAs(cut+"_nfatjetbtagM1.png");

        h15->SetTitle(cut+"_nfatjetbtagT1");
        h15->Draw();
        h15->Draw("TEXT0same");
        c1->SaveAs(cut+"_nfatjetbtagT1.png");

}
