#include "ExoDiBosonResonances/PATtupleProduction/plugins/NjettinessAdder.h"
#include "ExoDiBosonResonances/PATtupleProduction/interface/Njettiness.hh"

#include "FWCore/Framework/interface/MakerMacros.h"

void NjettinessAdder::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  // read input collection
  edm::Handle<edm::View<pat::Jet> > jets;
  iEvent.getByLabel(src_, jets);
  
  
  // prepare room for output
  std::vector<pat::Jet> outJets;   outJets.reserve(jets->size());

  for ( typename edm::View<pat::Jet>::const_iterator jetIt = jets->begin() ; jetIt != jets->end() ; ++jetIt ) {
    pat::Jet newCand(*jetIt);
    edm::Ptr<pat::Jet> jetPtr = jets->ptrAt(jetIt - jets->begin());
    newCand.addUserFloat("tau1", getTau(1, jetPtr ) );
    newCand.addUserFloat("tau2", getTau(2, jetPtr ) );
    newCand.addUserFloat("tau3", getTau(3, jetPtr ) );
// add tau4/5 etc
    newCand.addUserFloat("tau4", getTau(4, jetPtr ) );
    newCand.addUserFloat("tau5", getTau(5, jetPtr ) );

    outJets.push_back(newCand);
  }

  std::auto_ptr<std::vector<pat::Jet> > out(new std::vector<pat::Jet>(outJets));
  iEvent.put(out);
 
}

float NjettinessAdder::getTau(int num, edm::Ptr<pat::Jet> object) const
{
  std::vector<const reco::PFCandidate*> all_particles;
  if(object->isPFJet())
    {
      for (unsigned k =0; k < object->getPFConstituents().size(); k++)
	all_particles.push_back( object->getPFConstituent(k).get() );
    } else {
    for (unsigned j = 0; j < object->numberOfDaughters(); j++){
      reco::PFJet const *pfSubjet = dynamic_cast <const reco::PFJet *>(object->daughter(j));
      if (!pfSubjet) break;
          for (unsigned k =0; k < pfSubjet->getPFConstituents().size(); k++)
	    all_particles.push_back( pfSubjet->getPFConstituent(k).get() );	
    }
  }
  std::vector<fastjet::PseudoJet> FJparticles;
  for (unsigned particle = 0; particle < all_particles.size(); particle++){
    const reco::PFCandidate *thisParticle = all_particles.at(particle);
    FJparticles.push_back( fastjet::PseudoJet( thisParticle->px(), thisParticle->py(), thisParticle->pz(), thisParticle->energy() ) );	
  }
  NsubParameters paraNsub = NsubParameters(1.0, cone_); //assume R=0.7 jet clusering used
  Njettiness routine(Njettiness::onepass_kt_axes, paraNsub);
  return routine.getTau(num, FJparticles); 
}



DEFINE_FWK_MODULE(NjettinessAdder);
