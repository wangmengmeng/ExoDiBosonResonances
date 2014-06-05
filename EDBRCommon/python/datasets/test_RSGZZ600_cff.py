import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
##    '/store/cmst3/user/bonato//patTuple/2012/EXOVVtest/newPatTuple_ZZ_1000_c1.root'
#        '/store/cmst3/user/bonato//patTuple/2012/EXOVVtest/patExoWW_M600_10_1_KPf.root'
    #        '/store/cmst3/user/bonato//patTuple/2012/EXOVVtest/patZZ_M1000_5k_20121212.root'
#'file:/afs/cern.ch/user/b/bonato/scratch0/PhysAnalysis/EXOVV_2012/CMGTools/CMSSW_5_3_9/src/ExoDiBosonResonances/PATtupleProduction/python/patTuple.v2.root'
#    'file:/afs/cern.ch/user/b/bonato/scratch0/PhysAnalysis/EXOVV_2012/CMGTools/CMSSW_5_3_9/src/ExoDiBosonResonances/PATtupleProduction/python/patTuple_XWW.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/ExoDiBosonResonances/PATtupleProduction/python/pattuple_mwp1200_old.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/ExoDiBosonResonances/PATtupleProduction/python/pattuple_mwp1200_new.root'
#    'root://xrootd.unl.edu//store/user/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EXOWH_Wprime_M1000_PATtuple_cc_1204/69a9fa67eebd7bf7213e8a26a2d59023/pattuple_mwp1000_cc_1_1_5pv.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/pattuple_mwp1000cc_new.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/pattuple_mwp1000gg_new.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/pattuple_mwp1000bb_new.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/ExoDiBosonResonances/PATtupleProduction/python/pattuple_mwp1200_new.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/pattuple_M1000_test.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/SingleMu__Run2012A_test.root'
#    'file:/afs/cern.ch/work/m/mwang/public/EXO/1128/CMGTools/CMSSW_5_3_9/src/ExoDiBosonResonances/EDBRCommon/prod/DY.root'
#    'root://eoscms//eos/cms/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_DYToLLBinsPtZ_MADGRAPH_20140210_150636/mwang/DYJetsToLL_PtZ-100_TuneZ2star_8TeV_ext-madgraph-tarball/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/DYJetsToLL_PtZ-100_TuneZ2star_8TeV_ext-madgraph-tarball__Summer12_DR53X-PU_S10_START53_V7C-v1__AODSIM_1031_1_JwO.root'
    'file:/afs/cern.ch/work/m/mwang/public/ForJennifer/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_2_xXb.root'
#    'root://eoscms//eos/cms/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_SingleElectron_Run2012A-22Jan2013-v1/mwang/c2d529e1c78e50623ca40825abf53f99/SingleElectron__Run2012A-22Jan2013-v1__AOD_114_2_fIY.root'
#     '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_DYToLLBinsPtZ_MADGRAPH_20140210_150636/mwang/DYJetsToLL_PtZ-00_TuneZ2star_8TeV_ext-madgraph-tarball/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/DYJetsToLL_PtZ-100_TuneZ2star_8TeV_ext-madgraph-tarball__Summer12_DR53X-PU_S10_START53_V7C-v1__AODSIM_1181_1_VHx.root'
    ])
