import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
    	 'file:./smallsample/RSWW_AODSIM_9_1_8uc.root'
	)
)

process.demo = cms.EDAnalyzer('Gen_ana')



OUTPUT_FILE_NAME = "Graviton_genlevel.root"
process.TFileService = cms.Service(
    "TFileService", fileName = cms.string( OUTPUT_FILE_NAME ),
    closeFileFast = cms.untracked.bool(True)
)


process.p = cms.Path(process.demo)
