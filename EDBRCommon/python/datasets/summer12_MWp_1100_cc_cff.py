import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_Ysa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_zVj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_emD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_Rov.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_cvH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_Vt2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_UHn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_JHs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_ZIu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_1mw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_KSY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_LIs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_w7U.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_Rxq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_7UO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_GD3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_8mO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_fd1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_ewR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_3Jg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_UyT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_8mi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_n2O.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_hDG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_LVC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_oFj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_9da.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_yW8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_fTr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_AZI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_Cbm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_SUq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_KrG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_8Tl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_oG0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_ZSo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_E8R.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_ooX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_HWf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_lME.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_vls.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_CPB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_Aff.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_mNt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_Dln.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_E3Y.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_i9Z.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_bsB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_eJH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_08k.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1100_GENSIM_V2__mwang-EXOWH_Wprime_M1100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_cv0.root',
 ] )
