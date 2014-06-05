import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_HwS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_BGy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_oeR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_Psy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_bRm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_DPh.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_B6c.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_x5l.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_cqe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_gQ2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_cIg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_lyG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_GOH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_uCD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_0aW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_J7J.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_0yE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_7UT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_WKw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_HRZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_lyL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_pbD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_u0T.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_EBQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_Wqw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_1QU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_2wL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_w3m.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_tpk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_lVC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_OPp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_RAn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_KKO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_Mzc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_Rvb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_x1x.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_vhu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_vi1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_hYQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_5zS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_oHP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_4BV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_WNW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_SsY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_qce.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_0F8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_j0s.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_mkN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_ZM3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_Pxi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1900_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1900_GENSIM_V2__mwang-EXOWH_Wprime_M1900_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_5A7.root',
 ] )