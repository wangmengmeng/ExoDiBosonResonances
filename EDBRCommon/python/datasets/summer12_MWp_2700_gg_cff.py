import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_3_EBu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_3_uAi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_3_a1p.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_3_FyC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_3_EB6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_3_psT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_3_6GN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_3_eub.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_3_fsc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_3_tKv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_3_MR5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_3_ixT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_3_hQr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_3_VsH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_3_5JD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_3_6Bw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_3_YpA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_3_wl7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_3_hzg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_3_yk3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_3_dC6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_3_f8a.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_3_b9X.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_3_Neu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_3_1r5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_3_kRY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_3_yrT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_3_blO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_3_aV8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_3_LU3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_3_eiE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_3_vjS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_3_MbY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_3_xga.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_3_GaG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_3_Ezg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_3_rOL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_3_xm5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_3_apU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_3_qdi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_3_Qbx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_3_6kn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_3_Udf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_3_j0j.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_3_bTq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_3_Ofp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_3_N7g.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_gg_20140213_153713/mwang/EXOWH_Wprime_M2700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/0d71bd6eec2b8c7cc5eafcee05a85e30/EXOWH_Wprime_M2700_GENSIM_V2__mwang-EXOWH_Wprime_M2700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_3_czX.root',
 ] )
