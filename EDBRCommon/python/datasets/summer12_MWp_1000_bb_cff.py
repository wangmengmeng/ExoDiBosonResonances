import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_Qx6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_MAL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_7xG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_I6n.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_Saf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_mFt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_SH1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_Lla.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_anU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_KSB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_TVO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_dfX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_Y8i.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_LuU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_Dl9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_ldK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_RVd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_IBE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_vH2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_XYd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_akU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_sJZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_5j0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_lKB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_Ovl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_Srm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_3a0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_QLu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_8Mm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_jee.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_lN9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_vrT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_N2X.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_I2w.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_XAW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_ZQ2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_W2s.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_toi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_wyq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_iVM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_TDi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_GoH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_rxC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_swD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_MYf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_d0g.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_nJZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_Ltl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_8hD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_mvH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1000_GENSIM_V2__mwang-EXOWH_Wprime_M1000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_Hsd.root',
 ] )