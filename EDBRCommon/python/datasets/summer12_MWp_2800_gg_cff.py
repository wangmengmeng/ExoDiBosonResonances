import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_Gzi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_1hQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_sMC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_Rox.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_qDQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_UpI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_NUD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_HIW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_0yr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_GbI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_6BC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_h5g.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_HiZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_TlG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_9RC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_jM2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_F8x.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_wpC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_ovH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_dTf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_b04.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_Cn3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_ssz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_gU0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_fJe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_ets.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_RH2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_yHI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_MUK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_VNf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_wim.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_yGr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_6V4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_hMS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_tn4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_1Rt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_znG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_Cvt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_jzX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_Xpz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_6hb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_zOK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_Q8v.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_w6b.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_OZH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_OhT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_WqW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_R52.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_9Ls.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_kQO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_2_1Ar.root',
 ] )

