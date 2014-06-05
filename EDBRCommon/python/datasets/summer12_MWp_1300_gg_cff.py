import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_qnt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_5B8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_9Ic.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_u4H.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_G8t.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_pNl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_9NR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_fHJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_SXW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_NnD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_REH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_0Ee.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_49e.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_6U2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_ePW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_8cQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_WzR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_LpO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_WE3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_jq7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_zUM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_LcF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_a4U.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_eQy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_Ayc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_Q93.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_wyT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_D1l.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_QzF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_6Kf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_ZJu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_egl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_0DO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_YZQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_duE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_VXE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_xBa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_ErC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_kOA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_H6m.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_RJH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_iuI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_jRO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_ftj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_ks3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_hJ8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_wdE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_UHx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_oDZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_iJ7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1300_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1300_GENSIM_V2__mwang-EXOWH_Wprime_M1300_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_mOn.root',
 ] )

