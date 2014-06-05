import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_P2r.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_WsU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_U57.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_BQt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_t1j.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_o4S.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_ool.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_UjF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_EWm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_D0m.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_JIG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_xWY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_Pvq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_B5M.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_ZJ5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_Tzz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_d1F.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_AKi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_gSB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_Fv0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_1ZZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_dYX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_2zs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_VBz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_Bxj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_AJG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_UxX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_u1A.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_eqs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_omo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_uzB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_xpO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_EMB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_Jsi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_CqJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_rAn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_utt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_82w.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_gbY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_KPN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_XPB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_3F2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_GO8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_Vlb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_2UE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_n0D.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_lEK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_VAv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_qd9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_c2o.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2900_GENSIM_V2__mwang-EXOWH_Wprime_M2900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_CwU.root',
 ] )

