import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([

      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_4I9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_ZLW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_nVc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_3tb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_588.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_Uf9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_UnZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_SPG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_0pg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_z82.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_FR1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_QGI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_E6R.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_jd4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_L40.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_JPu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_MJV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_MCp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_9CG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_bzk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_4yO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_UU6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_xua.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_FSI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_bFi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_JYv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_hrh.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_nhz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_plO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_75E.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_tXJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_3hP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_jSN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_2OB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_S01.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_r8J.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_kuV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_fLw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_zII.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_sOg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_TK4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_wz5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_8gk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_9IC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_tTO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_ol9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_2UM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_5gD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_Qo5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_rq7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_CcL.root',
 ] )