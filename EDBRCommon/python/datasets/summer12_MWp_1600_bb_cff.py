import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_528.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_Ira.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_KkJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_r13.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_2pS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_JUG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_uQe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_O2p.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_PcH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_oXL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_S6y.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_AH8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_rQ7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_Nv4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_xK8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_93o.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_c1n.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_lfK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_fC8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_EHl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_gLQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_4gp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_Gx0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_HYD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_V5Q.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_uv8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_RdS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_jYW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_AhO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_Bun.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_BnX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_5WP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_tYj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_DuP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_SQS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_MVq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_exE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_KP3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_uMK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_3_nVh.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_3_qPr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_3_VoU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_3_dV3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_WvX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_Rs4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_h6D.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_YEP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_5C4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_Irj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_iN8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1600_GENSIM_V2__mwang-EXOWH_Wprime_M1600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_OUt.root',
 ] )