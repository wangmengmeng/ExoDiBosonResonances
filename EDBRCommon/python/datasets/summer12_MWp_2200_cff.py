import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([

       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_kkk.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_WyB.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_rTW.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_hwM.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_GXt.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_hpG.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_Bp5.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_rrO.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_Z3Z.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_xc4.root',
       '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140114_Summer12MC_WprimeWH_20140115_101708/mwang/EXOWH_Wprime_M2200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140114/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2200_GENSIM_V2__mwang-EXOWH_Wprime_M2200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_oYB.root',

 ] )
