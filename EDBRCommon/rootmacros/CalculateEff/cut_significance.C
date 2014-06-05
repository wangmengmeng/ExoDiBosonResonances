#include <vector>
#include "TH1.h"
#include "TString.h"
#include "TFile.h"
#include "TTree.h"
#include <iostream>
#include "TCanvas.h"
#include "TStyle.h"

void cut_significance()
{
	//	TString inputpath = "/afs/cern.ch/work/m/mwang/public/EDBR/trees/productionv1_1130/fullrange/";
	TString inputpath = "/afs/cern.ch/work/m/mwang/public/EDBR/trees/productionv1_0319/fullrange/";
	TString cut = "btag_significance_";
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

	int ndata = 0; //dataSamples.size();
	int nbkg  = bkgSamples.size();
	int nsig  = sigSamples.size();

	cout<<"data samples "<<ndata<<"  bkg samples "<<nbkg<<"  signal samples "<<nsig<<endl;	

	//TH1F * h1 = new TH1F (cut,cut,ndata+nbkg+nsig+1,0,ndata+nbkg+nsig+1);
	TH1F * h1 = new TH1F (cut,cut,15 ,0,15); //== number of cut selections
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
	TH1F *h12 = (TH1F*)h1->Clone(cut+"_12"); //== number of signal MC samples
	/*        TH1F *h13 = (TH1F*)h1->Clone(cut+"_13");
		  TH1F *h14 = (TH1F*)h1->Clone(cut+"_14");
		  TH1F *h15 = (TH1F*)h1->Clone(cut+"_15");
		  TH1F *h16 = (TH1F*)h1->Clone(cut+"_16");
		  TH1F *h17 = (TH1F*)h1->Clone(cut+"_17");
		  TH1F *h18 = (TH1F*)h1->Clone(cut+"_18");
	 */
	TCanvas * c1 = new TCanvas();	

	double totalB1=0;
	double totalB2=0;
	double totalB3=0;
	double totalB4=0;
	double totalB5=0;
	double totalB6=0;
	double totalB7=0;
	double totalB8=0;
	double totalB9=0;
	double totalB10=0;
	double totalB11=0;
	double totalB12=0;
	double totalB13=0;
	double totalB14=0;
	double totalB15=0;
	double sigeff1[30];
	double sigeff2[30];
	double sigeff3[30];
	double sigeff4[30];
	double sigeff5[30];
	double sigeff6[30];
	double sigeff7[30];
	double sigeff8[30];
	double sigeff9[30];
	double sigeff10[30];
	double sigeff11[30];
	double sigeff12[30];
	double sigeff13[30];
	double sigeff14[30];
	double sigeff15[30];

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
			eff11 = (double)pass10/(double)total;
			eff12 = (double)pass10/(double)total;
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

		if(i>=ndata&&i<(ndata+nbkg))//for bkg, sum all passed
		{
			totalB1=totalB1+pass1;
			totalB2=totalB2+pass2;
			totalB3=totalB3+pass3;
			totalB4=totalB4+pass4;
			totalB5=totalB5+pass5;
			totalB6=totalB6+pass6;
			totalB7=totalB7+pass7;
			totalB8=totalB8+pass8;
			totalB9=totalB9+pass9;
			totalB10=totalB10+pass10;
			totalB11=totalB11+pass11;
			totalB12=totalB12+pass12;
			totalB13=totalB13+pass13;
			totalB14=totalB14+pass14;
			totalB15=totalB15+pass15;
		}
		if(i>=(ndata+nbkg))//for signal, save the efficiency
		{
			sigeff1[i-ndata-nbkg]=eff1;
			sigeff2[i-ndata-nbkg]=eff2;
			sigeff3[i-ndata-nbkg]=eff3;
			sigeff4[i-ndata-nbkg]=eff4;
			sigeff5[i-ndata-nbkg]=eff5;
			sigeff6[i-ndata-nbkg]=eff6;
			sigeff7[i-ndata-nbkg]=eff7;
			sigeff8[i-ndata-nbkg]=eff8;
			sigeff9[i-ndata-nbkg]=eff9;
			sigeff10[i-ndata-nbkg]=eff10;
			sigeff11[i-ndata-nbkg]=eff11;
			sigeff12[i-ndata-nbkg]=eff12;
			sigeff13[i-ndata-nbkg]=eff13;
			sigeff14[i-ndata-nbkg]=eff14;
			sigeff15[i-ndata-nbkg]=eff15;
		}


	}//end of sample loop


	c1->SetGridy(1);

	for(int i =0; i<nsig; i++   )
	{
		TString filename;
		TString samplename;
		filename = "treeEDBR_"+sigSamples.at(i)+".root";
		samplename = sigSamples.at(i);
		samplename.Remove(samplename.Length()-4,4);

		if(i==0)
		{
			h1->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h1->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h1->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h1->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h1->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h1->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h1->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h1->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h1->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h1->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h1->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h1->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h1->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h1->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h1->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h1->SetTitle(cut+samplename);
			h1->Draw();
			h1->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==1)
		{
			h2->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h2->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h2->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h2->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h2->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h2->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h2->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h2->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h2->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h2->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h2->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h2->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h2->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h2->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h2->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h2->SetTitle(cut+samplename);
			h2->Draw();
			h2->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==2)
		{
			h3->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h3->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h3->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h3->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h3->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h3->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h3->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h3->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h3->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h3->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h3->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h3->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h3->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h3->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h3->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h3->SetTitle(cut+samplename);
			h3->Draw();
			h3->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==3)
		{
			h4->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h4->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h4->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h4->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h4->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h4->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h4->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h4->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h4->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h4->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h4->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h4->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h4->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h4->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h4->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h4->SetTitle(cut+samplename);
			h4->Draw();
			h4->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==4)
		{
			h5->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h5->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h5->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h5->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h5->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h5->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h5->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h5->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h5->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h5->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h5->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h5->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h5->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h5->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h5->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h5->SetTitle(cut+samplename);
			h5->Draw();
			h5->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==5)
		{
			h6->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h6->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h6->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h6->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h6->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h6->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h6->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h6->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h6->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h6->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h6->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h6->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h6->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h6->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h6->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h6->SetTitle(cut+samplename);
			h6->Draw();
			h6->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==6)
		{
			h7->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h7->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h7->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h7->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h7->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h7->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h7->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h7->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h7->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h7->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h7->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h7->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h7->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h7->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h7->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h7->SetTitle(cut+samplename);
			h7->Draw();
			h7->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==7)
		{
			h8->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h8->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h8->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h8->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h8->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h8->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h8->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h8->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h8->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h8->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h8->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h8->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h8->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h8->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h8->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h8->SetTitle(cut+samplename);
			h8->Draw();
			h8->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==8)
		{
			h9->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h9->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h9->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h9->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h9->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h9->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h9->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h9->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h9->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h9->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h9->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h9->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h9->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h9->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h9->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h9->SetTitle(cut+samplename);
			h9->Draw();
			h9->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==9)
		{
			h10->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h10->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h10->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h10->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h10->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h10->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h10->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h10->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h10->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h10->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h10->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h10->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h10->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h10->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h10->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h10->SetTitle(cut+samplename);
			h10->Draw();
			h10->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==10)
		{
			h11->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h11->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h11->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h11->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h11->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h11->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h11->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h11->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h11->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h11->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h11->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h11->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h11->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h11->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h11->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h11->SetTitle(cut+samplename);
			h11->Draw();
			h11->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
		if(i==11)
		{
			h12->Fill("nsubjetbtagL0",sigeff1[i]/(1+sqrt(totalB1)));
			h12->Fill("nsubjetbtagM0",sigeff2[i]/(1+sqrt(totalB2)));
			h12->Fill("nsubjetbtagT0",sigeff3[i]/(1+sqrt(totalB3)));
			h12->Fill("nsubjetbtagL1",sigeff4[i]/(1+sqrt(totalB4)));
			h12->Fill("nsubjetbtagM1",sigeff5[i]/(1+sqrt(totalB5)));
			h12->Fill("nsubjetbtagT1",sigeff6[i]/(1+sqrt(totalB6)));
			h12->Fill("nsubjetbtagL2",sigeff7[i]/(1+sqrt(totalB7)));
			h12->Fill("nsubjetbtagM2",sigeff8[i]/(1+sqrt(totalB8)));
			h12->Fill("nsubjetbtagT2",sigeff9[i]/(1+sqrt(totalB9)));
			h12->Fill("nfatjetbtagL0",sigeff10[i]/(1+sqrt(totalB10)));
			h12->Fill("nfatjetbtagM0",sigeff11[i]/(1+sqrt(totalB11)));
			h12->Fill("nfatjetbtagT0",sigeff12[i]/(1+sqrt(totalB12)));
			h12->Fill("nfatjetbtagL1",sigeff13[i]/(1+sqrt(totalB13)));
			h12->Fill("nfatjetbtagM1",sigeff14[i]/(1+sqrt(totalB14)));
			h12->Fill("nfatjetbtagT1",sigeff15[i]/(1+sqrt(totalB15)));
			h12->SetTitle(cut+samplename);
			h12->Draw();
			h12->Draw("TEXT0same");
			c1->SaveAs(cut+samplename+".png");
		}
	}


}
