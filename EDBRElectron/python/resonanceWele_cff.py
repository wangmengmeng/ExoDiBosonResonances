import FWCore.ParameterSet.Config as cms

from ExoDiBosonResonances.EDBRElectron.factories.cmgWelenuDiJet_cfi import * 
from ExoDiBosonResonances.EDBRElectron.factories.cmgWelenuSingleJet_cfi import *

from ExoDiBosonResonances.EDBRElectron.skims.cmgEDBRSel_Wele_cff import *
from ExoDiBosonResonances.EDBRElectron.skims.selEventsEDBR_cfi import *
from ExoDiBosonResonances.EDBRElectron.HLTWeights_Wele_cff import *
from ExoDiBosonResonances.EDBRElectron.BTagWeights_Wele_cff import *

### add pu weights for run 2012A
cmgEDBRKinFitWeighted2012A = cms.EDProducer("WelenuDiJetEDBRWeightAdder",
                                        src=cms.InputTag("BTagWeightsKinFitEle"),
                                        weight=cms.InputTag("PUWeights2012A"),
                                        )   
cmgEDBRWeighted2012A = cms.EDProducer("WelenuDiJetEDBRWeightAdder",
                                  src=cms.InputTag("BTagWeightsEle"),
                                  weight=cms.InputTag("PUWeights2012A"),
                                  )   

cmgEDBRMergedWeighted2012A = cms.EDProducer("WelenuSingleJetEDBRWeightAdder",
                                  src=cms.InputTag("BTagWeightsMergedEle"),
                                  weight=cms.InputTag("PUWeights2012A")
                                  )   

### add pu weights for run 2012B
cmgEDBRKinFitWeighted2012B = cms.EDProducer("WelenuDiJetEDBRWeightAdder",
                                        src=cms.InputTag("cmgEDBRKinFitWeighted2012A"),
                                        weight=cms.InputTag("PUWeights2012B"),
                                        )   
cmgEDBRWeighted2012B = cms.EDProducer("WelenuDiJetEDBRWeightAdder",
                                  src=cms.InputTag("cmgEDBRWeighted2012A"),
                                  weight=cms.InputTag("PUWeights2012B"),
                                  )   
cmgEDBRMergedWeighted2012B = cms.EDProducer("WelenuSingleJetEDBRWeightAdder",
                                  src=cms.InputTag("cmgEDBRMergedWeighted2012A"),
                                  weight=cms.InputTag("PUWeights2012B"),
                                  )   

### add pu weights for run 2012 A+B
cmgEDBRKinFitWeighted = cms.EDProducer("WelenuDiJetEDBRWeightAdder",
                                        src=cms.InputTag("cmgEDBRKinFitWeighted2012B"),
                                        weight=cms.InputTag("PUWeights"),
                                        )   
cmgEDBRWeighted = cms.EDProducer("WelenuDiJetEDBRWeightAdder",
                                  src=cms.InputTag("cmgEDBRWeighted2012B"),
                                  weight=cms.InputTag("PUWeights"),
                                  )
cmgEDBRMergedWeighted = cms.EDProducer("WelenuSingleJetEDBRWeightAdder",
                                  src=cms.InputTag("cmgEDBRMergedWeighted2012B"),
                                  weight=cms.InputTag("PUWeights"),
                                  )

#### add extra-kinematic variables to EDBR candidate (only the one with kin-fit)
cmgEDBRExtra = cms.EDProducer("WelenuDiJetEDBRKineAdder",
                              src=cms.InputTag("cmgEDBRKinFitWeighted"),
                              noKinFitSrc=cms.InputTag("cmgEDBRWeighted"), #leave empty if SingleJet EDBR
                              BTagJets=cms.InputTag("jetAK5"),
                              BTagCleaningTarget=cms.InputTag("jetIDJet")                                
            
                                   )

cmgEDBRMergedExtra = cms.EDProducer("WelenuSingleJetEDBRKineAdder",
                                   src=cms.InputTag("cmgEDBRMergedWeighted"),
                                   noKinFitSrc=cms.InputTag(""), #leave empty if SingleJet EDBR
                                    BTagJets=cms.InputTag("jetAK5"),
                                    BTagCleaningTarget=cms.InputTag("jetIDJet")    
                                   )

edbrSequenceEVJJ = cms.Sequence(
    cmgWelenuDiJet +
    cmgWelenuDiJetKinFit +

    cmgWelenuDiJetEDBR +
    cmgWelenuDiJetKinFitEDBR +

    HLTWeightsEle +
    HLTWeightsKinFitEle +

    BTagWeightsEle +
    BTagWeightsKinFitEle +

    cmgEDBRKinFitWeighted2012A +
    cmgEDBRWeighted2012A +
    cmgEDBRKinFitWeighted2012B +
    cmgEDBRWeighted2012B +
    cmgEDBRKinFitWeighted +
    cmgEDBRWeighted +

    cmgEDBRExtra+
    cmgEDBRSel +
    cmgEDBRSelKinFit

#    selectedEDBRKinFitCandFilter 
    #selectedEDBRCandFilter


)

edbrSequenceMergedEVJ = cms.Sequence(
    cmgWelenuSingleJet +
    cmgWelenuSingleJetEDBR +

    HLTWeightsMergedEle +

    BTagWeightsMergedEle +

    cmgEDBRMergedWeighted2012A +
    cmgEDBRMergedWeighted2012B +
    cmgEDBRMergedWeighted +
    cmgEDBRMergedExtra+
    cmgEDBRMergedSel
 #   selectedEDBRMergedCandFilter


    )
         
