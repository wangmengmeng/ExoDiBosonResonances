import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_3_OsI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_3_E2r.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_3_OSg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_3_L4N.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_3_wOL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_3_Fb4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_3_Rat.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_3_sEJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_3_52u.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_3_vwd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_3_9M7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_3_qNO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_3_sqv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_3_KKQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_3_4U3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_3_BkU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_3_Oty.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_3_f7K.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_3_PM4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_3_nb4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_3_yob.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_3_VY7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_3_S7x.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_3_03S.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_3_iZ0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_3_ite.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_3_K7K.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_3_h5l.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_3_Xqc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_3_Ja5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_3_dGc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_3_Mu4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_3_SwL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_3_RZ1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_3_RrK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_3_sJF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_3_txn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_3_zZY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_3_hjt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_3_GZ7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_3_ljD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_3_w9v.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_3_Qsm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_3_3DW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_3_r5u.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_3_lI7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_3_0y4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_3_0TK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_3_2fR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_3_xhs.root',
 ] )
