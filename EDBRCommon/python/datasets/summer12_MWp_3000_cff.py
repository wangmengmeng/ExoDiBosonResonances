import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([

      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_2_q33.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_2_hj9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_2_R4M.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_2_SkO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_2_YUV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_2_jBR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_2_F5j.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_2_cea.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_2_tkO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_2_809.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_2_McI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_2_KUA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_2_wp8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_2_NDd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_2_z4Q.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_2_Kq9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_2_2mW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_2_RNa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_2_KTq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_2_xSd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_3_SnQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_2_2PX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_2_VoY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_2_5yg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_2_sqQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_2_6CX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_2_KKJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_2_YTV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_2_NLE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_2_46K.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_2_NI0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_2_T6Y.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_2_x4h.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_2_fXz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_2_Rmy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_2_ZOr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_2_QlX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_2_rT5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_2_Wus.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_2_a17.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_2_9wb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_2_Y8a.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_2_Hyi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_2_xID.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_2_UwN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_2_lyT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_2_3jo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_2_pbD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_2_DCz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M3000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M3000_GENSIM_V2__mwang-EXOWH_Wprime_M3000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_2_jAU.root',
 ] )