import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_3_6kp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_3_btn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_3_13D.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_3_7kB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_3_hGL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_3_sUM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_3_gSN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_3_lZU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_2_OQ7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_3_hJL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_3_Qo7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_3_uqm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_3_Jl6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_BHJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_Fjz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_XDS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_1Ci.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_GVZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_okM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_dmW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_b4y.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_3_fNE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_LD3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_lH8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_K2a.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_5Fo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_wLe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_FN7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_uEV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_lAn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_wbs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_7qg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_3_2cc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_MgV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_N74.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_QfN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_cYA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_aWy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_XwK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_0Hs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_CLF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_GSB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_sX3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_2_9cB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_flV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_3Cl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_2_0hH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_3_laG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_3_wXW.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_3_1aE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M2000_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M2000_GENSIM_V2__mwang-EXOWH_Wprime_M2000_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_3_SRB.root',
 ] )