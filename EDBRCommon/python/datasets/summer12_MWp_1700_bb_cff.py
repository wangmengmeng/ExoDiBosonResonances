import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_itg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_S9x.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_kFr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_TsT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_vkL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_doU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_jw7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_lfH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_i0R.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_5fu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_Km2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_MNQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_6Vs.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_KCP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_0wa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_y8N.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_3EE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_nUP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_kDJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_KkC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_oTS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_vxZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_6MZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_MYe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_uwi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_eO3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_upK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_AWf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_ctA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_QLO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_Af1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_hoA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_2Mr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_n9T.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_rSP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_oDo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_Cvx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_KAn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_zuJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_DGc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_XOY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_OQp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_iRf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_RTA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_mkC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_EMJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_FUw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_jJV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_HLB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_SbI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1700_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1700_GENSIM_V2__mwang-EXOWH_Wprime_M1700_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_QfN.root',
 ] )
