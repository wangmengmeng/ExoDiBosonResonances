#from CMGTools.Common.electron_cff import *
from ExoDiBosonResonances.EDBRElectron.factories.cmgElectron_cfi import *


genSelectorZDaughterE = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag("genParticles"),
    cut = cms.string(' (abs(pdgId)==11 )&& abs(mother.pdgId)==23 ')
)
genSelectorWDaughterE = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag("genParticles"),
    cut = cms.string(' (abs(pdgId)==11 )&& abs(mother.pdgId)==24 ')
)

selectedPatElectrons  = cms.EDProducer("PATElectronCleaner",
                                        src = cms.InputTag("patElectronsWithTrigger"), #selectedPatElectronsAK5
                                        preselection = cms.string(''),
                                        checkOverlaps = cms.PSet( genLeptons = cms.PSet( src = cms.InputTag("genSelectorZDaughterE"),
                                                                                         algorithm = cms.string("byDeltaR"),
                                                                                         preselection        = cms.string(""),  # don't preselect the muons
                                                                                         deltaR              = cms.double(0.3),
                                                                                         checkRecoComponents = cms.bool(False), # don't check if they share some AOD object ref
                                                                                         pairCut             = cms.string(""),
                                                                                         requireNoOverlaps = cms.bool(False), # overlaps don't cause the electron to be discared
                                                                                         ),
                                                                  genLeptonsW = cms.PSet( src = cms.InputTag("genSelectorWDaughterE"),
                                                                                         algorithm = cms.string("byDeltaR"),
                                                                                         preselection        = cms.string(""),  # don't preselect the muons
                                                                                         deltaR              = cms.double(0.3),
                                                                                         checkRecoComponents = cms.bool(False), # don't check if they share some AOD object ref
                                                                                         pairCut             = cms.string(""),
                                                                                         requireNoOverlaps = cms.bool(False), # overlaps don't cause the electron to be discared
                                                                                         ),
                                                                  ),                                      
                                        finalCut = cms.string(''),
                                        )



#cmgElectron.cfg.inputCollection="selectedPatElectrons"
# ele ID requirements
#cmgElectron.cuts.mvaTrigSel =mvaTrigEleId.clone() 
#cmgElectron.cuts.cutBasedVeto = cutBasedVetoEleId.clone()
#cmgElectron.cuts.cutBasedLoose = cutBasedLooseEleId.clone()
#cmgElectron.cuts.conversionVeto = cms.PSet(
#    patFlag=cms.string('sourcePtr().passConversionVeto()')    
#    )

### Isolation requirements (also embedded in CombIsoVBTFXX and wp95c)
#cmgElectron.cuts.reliso = cms.PSet ( reliso = cms.string(" (sourcePtr.get.dr03HcalTowerSumEt + sourcePtr.get.dr03EcalRecHitSumEt + sourcePtr.get.dr03TkSumPt) / et < 0.15 ") )


### kinematic requirements
#cmgElectron.cuts.kinematics = eKinematics.clone()

### MC matching
#cmgElectron.cuts.genLepton = cms.PSet( genLepton = cms.string("sourcePtr().get().hasOverlaps('genLeptons')"))
 
eleSequence = cms.Sequence(genSelectorZDaughterE + genSelectorWDaughterE  + selectedPatElectrons + cmgElectron)

