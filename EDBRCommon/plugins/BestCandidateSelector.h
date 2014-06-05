#ifndef ExoDiBosonResonances_EDBRCommon_BestCandidateSelector_h
#define ExoDiBosonResonances_EDBRCommon_BestCandidateSelector_h

#include <TF1.h>

template<class type1, class type2>
class BestCandidateSelector : public edm::EDProducer {
	public:
		explicit BestCandidateSelector(const edm::ParameterSet& iConfig) :
			srcSingleJet_(iConfig.getParameter<edm::InputTag>("srcSingleJet")),
			srcDoubleJet_(iConfig.getParameter<edm::InputTag>("srcDoubleJet")),
//			VMass_(iConfig.getParameter<double>("VMass")),
// change here for WH analysis
                        VMass1_(iConfig.getParameter<double>("VMass1")),
                        VMass2_(iConfig.getParameter<double>("VMass2")),

			Algo_(iConfig.getParameter<std::string>("Algo")),
			priorityList_(iConfig.getParameter<std::vector<std::string> >("tagSelectionList"))
	{
		produces<std::vector<type1> >("singleJet"); //
		produces<std::vector<type2> >("doubleJet"); //

		if(Algo_=="UseVMass")
		{
			useBestZMass_=true;
			useHighestJetPt_=false;
			useTTSelection_=false;
		}
		else if(Algo_=="UseJetPt")
		{
			useBestZMass_=false;
			useHighestJetPt_=true;
			useTTSelection_=false;
		}
		else if(Algo_=="UseTTBar")
		{   
			useBestZMass_=false;
			useHighestJetPt_=false;
			useTTSelection_=true;
		}   
		else std::cout<<"Wrong Algo! Should be UseVMass or UseJetPt or UseTTBar!!"<<std::endl;
	}

		virtual ~BestCandidateSelector() {}

		void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) ;

	private:
		edm::InputTag srcSingleJet_ ;
		edm::InputTag srcDoubleJet_ ;
//		double VMass_;
// also change here for WH analysis
                double VMass1_, VMass2_;

		std::string Algo_;

		std::vector<std::string> priorityList_;
		bool useBestZMass_;
		bool useHighestJetPt_;
		bool useTTSelection_;

};

template <class type1, class type2>
void BestCandidateSelector<type1, type2>::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {

	edm::Handle<edm::View<type1> > edbr1Jcands;
	iEvent.getByLabel(srcSingleJet_, edbr1Jcands);

	edm::Handle<edm::View<type2> > edbr2Jcands;
	iEvent.getByLabel(srcDoubleJet_, edbr2Jcands);

	// prepare room for output
	std::vector<type1> out1JCands;   
	std::vector<type2> out2JCands;

	unsigned int bestindex=9999;
	float bestDiff =99999999;
//	const float nomZmass=VMass_;
// change here for WH analysis
	const float nomWmass=VMass1_;
	const float nomHmass=VMass2_;

	double highestPt =0.;
	bool found = false;
	double highestMass =0.;

	std::vector<int>   bestByCategory; 
	bestByCategory.reserve(priorityList_.size()) ;  
	bestByCategory.assign(priorityList_.size(),9999);

	std::vector<float> diffByCategory; 
	diffByCategory.reserve(priorityList_.size()) ;  
	diffByCategory.assign(priorityList_.size(),99999999);

	int nSel=0,nSel1J=0,nSel2J=0;  
	for(unsigned int cat = 0 ; cat <  priorityList_.size() ; cat++){
		//once you found a good cand in the top list
		//skip the following categories
		if(nSel>0)continue;


		for (unsigned int i=0 ; i<edbr1Jcands->size() ; ++i ) {
			edm::RefToBase<type1>  edbrCand = edbr1Jcands->refAt(i);

			if(! edbrCand->getSelection(priorityList_[cat]))continue;

			//compute mass differences
			float leptonicMass = edbrCand->leg1().mass();
			float quarkMass = edbrCand->leg2().prunedMass();
//			float diff = (leptonicMass - nomZmass)*(leptonicMass - nomZmass) + (quarkMass - nomZmass)*(quarkMass - nomZmass);
// change here for WH analysis
			float diff = (leptonicMass - nomWmass)*(leptonicMass - nomWmass) + (quarkMass - nomHmass)*(quarkMass - nomHmass);

			double jetPt = edbrCand->leg2().pt();


			if( useBestZMass_ && (diff < bestDiff)){//new best candidate found
				found = true;
				bestDiff = diff;
				bestindex = i;
			} 
			else if(useHighestJetPt_&& (jetPt>highestPt) )
			{
				found = true;
				highestPt = jetPt;
				bestindex = i;
			}
			else if( useTTSelection_ && (   (jetPt<200&&jetPt>highestPt) || (jetPt>=200&& quarkMass>highestMass)  )    )
			{
				found = true;
				highestPt = jetPt;
				highestMass = quarkMass;
				bestindex = i;

			}

			/**** //no BTAG for the moment
			  if(doBtag_){// look for best candidates separately by category
			  for(unsigned int cat = 0 ; cat <  priorityList_.size() ; cat++){
			  if(edbrCand->getSelection(priorityList_[cat])){
			  if(diff < diffByCategory[cat]){
			  diffByCategory[cat]= diff;
			  bestByCategory[cat]= i;
			  }
			  } 
			  }
			  }
			 **********/

		}//end loop on type1 collection

		if(found){ nSel++; nSel1J++; }

		/////now loop on EDBR-Dijet collection
		found=false;
		for (unsigned int i=0 ; i<edbr2Jcands->size() ; ++i ) {
			edm::RefToBase<type2>  edbrCand2 = edbr2Jcands->refAt(i);

			if(! edbrCand2->getSelection(priorityList_[cat]))continue;

			//compute mass differences
			float leptonicMass = edbrCand2->leg1().mass();
			float quarkMass = (edbrCand2->leg2().leg1().sourcePtr()->get()->p4() + edbrCand2->leg2().leg2().sourcePtr()->get()->p4()).M();
//			float diff = (leptonicMass - nomZmass)*(leptonicMass - nomZmass) + (quarkMass - nomZmass)*(quarkMass - nomZmass);
// change here for WH analysis
			float diff = (leptonicMass - nomWmass)*(leptonicMass - nomWmass) + (quarkMass - nomHmass)*(quarkMass - nomHmass);

			double jetPt = edbrCand2->leg2().leg1().pt()+edbrCand2->leg2().leg2().pt();


			if( useBestZMass_ && (diff < bestDiff)){//new best candidate found
				found = true;
				bestDiff = diff;
				bestindex = i;
			}

			else if( useHighestJetPt_&& (jetPt>highestPt) )
			{
				found = true;
				highestPt = jetPt;
				bestindex = i;
			}
			else if( useTTSelection_ && (   (jetPt<200&&jetPt>highestPt) || (jetPt>=200&& quarkMass>highestMass)  )    )
			{
				found = true;
				highestPt = jetPt;
				highestMass = quarkMass;
				bestindex = i;

			}


		}//end loop on type2 collection

		if(found){ nSel++; nSel2J++;}



	}//end loop on tag priority list


	if(nSel>1){
		throw cms::Exception("Logical error")<<"Error in BestCandidateSelector, nSel should be exactly equal to one. nSel="<<nSel<<std::endl;

	}

	if(nSel==1){// cuts passed! => save candidate
		if(nSel1J>0){
			type1 new1JCand(*(edbr1Jcands->refAt(bestindex)));
			out1JCands.push_back( new1JCand );
		}

		if(nSel2J>0){
			type2 new2JCand(*(edbr2Jcands->refAt(bestindex)));
			out2JCands.push_back( new2JCand );
		}
	}

	std::auto_ptr<std::vector<type1> > out1Jcoll(new std::vector<type1>(out1JCands));
	std::auto_ptr<std::vector<type2> > out2Jcoll(new std::vector<type2>(out2JCands));
	iEvent.put(out1Jcoll,"singleJet");
	iEvent.put(out2Jcoll,"doubleJet");

}
#endif
