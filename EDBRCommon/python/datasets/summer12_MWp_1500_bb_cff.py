import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_Gle.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_aK4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_e3W.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_lLk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_VeK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_Y1j.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_QN2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_5Il.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_JMd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_WNO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_mVF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_CBH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_hdV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_88t.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_yeD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_z2A.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_2lw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_9DI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_n4S.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_KKU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_u14.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_ZEg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_gK9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_X2Z.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_mC0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_aJd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_Ung.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_5BG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_Le8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_qTx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_kqq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_p5z.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_Gbo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_vQ0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_G1R.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_NPa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_RqT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_Md0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_jUj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_t9t.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_AzG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_nku.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_NBn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_VWx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_DSq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_61e.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_5ew.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_KVO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_BTm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1500_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1500_GENSIM_V2__mwang-EXOWH_Wprime_M1500_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_281.root',
 ] )
