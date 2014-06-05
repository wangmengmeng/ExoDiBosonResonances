import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_JBj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_t70.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_q4T.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_bzw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_Jah.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_xyy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_j1L.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_A46.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_iAc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_9sI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_nFA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_E5V.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_vCO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_OF2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_a4B.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_C33.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_tKT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_zsk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_NBM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_5x9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_3Ln.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_coV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_ZMN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_T9A.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_dwH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_w4p.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_o5u.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_1Tn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_W5u.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_INn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_0eU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_gsu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_4Ec.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_crP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_ds1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_LKf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_Mwi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_AIA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_GNt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_2qT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_M6p.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_4rW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_Ifu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_UiC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_rUd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_Ylo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_3YA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_YKK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_E1H.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_wQ9.root',
 ] )
