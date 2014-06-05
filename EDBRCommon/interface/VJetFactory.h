#ifndef _ExoDiBosonResonances_EDBRCommon_VJetFactory_h_
#define _ExoDiBosonResonances_EDBRCommon_VJetFactory_h_

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "AnalysisDataFormats/ExoDiBosonResonances/interface/VJet.h"
#include "CMGTools/Common/interface/Factory.h"
#include "CMGTools/Common/interface/PFJetFactory.h"

#include <iostream>
#include <memory>

namespace cmg{

class VJetFactory : public Factory<cmg::VJet>{
  public:
    VJetFactory(const edm::ParameterSet& ps);
    
    virtual event_ptr create(const edm::Event&, const edm::EventSetup&);
    void set(const edm::Event& iEvent, const edm::EventSetup& iSetup,
			  const pat::JetPtr& input, cmg::VJet *output);

    float JetResolution(const edm::Event& iEvent, cmg::VJet *output);

  private:
    const edm::InputTag jetLabel_;
    const edm::InputTag prunedJetLabel_;
// add subjet for WH
    const edm::InputTag subJetLabel_;
/*
    struct JetRefCompare :
      public std::binary_function<edm::RefToBase<reco::Jet>, edm::RefToBase<reco::Jet>, bool> {
      inline bool operator () (const edm::RefToBase<reco::Jet> &j1,
       			       const edm::RefToBase<reco::Jet> &j2) const
      { return j1.id() < j2.id() || (j1.id() == j2.id() && j1.key() < j2.key()); }
    };
    typedef std::map<edm::RefToBase<pat::Jet>, unsigned int, JetRefCompare> FlavourMap;
*/

    const BaseJetFactory baseJetFactory_;
    const PFJetFactory pfJetFactory_;
    edm::InputTag puVariablesTag_;
    std::vector< edm::InputTag > puMvasTag_, puIdsTag_,puNamesTag_;
    const bool useConstituents_;
    const bool verbose_;

    const bool applyResolution_;
    const bool applyScale_, applyScaleDB_;
    const std::string scaleFile_;
    const double nSigmaScale_;

  };

}


#endif
