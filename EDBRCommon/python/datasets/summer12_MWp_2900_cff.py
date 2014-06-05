import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([

      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_31m.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_qB6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_Jy7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_afb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_AzK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_noB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_WK3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_qEu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_cC2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_4TJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_3_X4z.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_Vu3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_Q99.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_VDX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_eWu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_s2E.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_p1o.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_L2T.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_9rf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_Fv1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_8SR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_ZzV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_SoE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_8Zv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_SYE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_oCj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_cEA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_8hg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_5BB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_KA1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_vgQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_jpq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_Bl0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_Ogm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_TCF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_zuO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_tTn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_B9W.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_z76.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_Vdk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_pK2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_2RE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_0IU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_N13.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_jaN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_sTf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_ndc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_Sit.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_TDj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_rYd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_osN.root',
 ] )
