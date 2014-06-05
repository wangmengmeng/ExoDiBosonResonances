import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_2bX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_yek.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_TuP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_Ug1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_Eea.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_N5E.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_YUp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_Aij.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_jiJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_StA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_BJt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_cfs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_Rg0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_NjJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_ImT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_DdB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_Yje.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_ah7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_CuR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_VFS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_9SI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_pPE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_c0L.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_pyG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_77M.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_yJC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_QjT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_ieJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_0BR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_Byo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_7n8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_vAH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_ynG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_EKA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_6vr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_EPp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_EUD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_lo7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_6sT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_0FR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_bDq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_pM3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_hIB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_Aw3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_Ed0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_xWR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_Kbe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_3RW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_QwE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_xZ8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M270_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_HgZ.root',
 ] )
