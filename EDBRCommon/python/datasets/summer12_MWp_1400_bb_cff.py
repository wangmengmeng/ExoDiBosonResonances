import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_Mo8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_yk4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_iba.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_4dM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_HzF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_MW7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_iiB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_Xtz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_1w2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_QVV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_wmR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_GGt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_CWy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_Hqg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_0pe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_T3L.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_ub5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_Hv4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_Veg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_YyF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_yYq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_MJP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_epF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_Gkz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_Y2h.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_pXA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_Jxc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_hay.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_07Q.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_PmS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_p4q.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_gQC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_qon.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_1tJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_naO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_l6a.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_Ga3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_GU7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_wI5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_Jwl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_Av9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_N9y.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_IWI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_rlz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_lnn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_Sq9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_SoJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_srC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_Cmr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_cLU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_bb_20140213_153901/mwang/EXOWH_Wprime_M1400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/3420c765efd533572b36b45c18b0a836/EXOWH_Wprime_M1400_GENSIM_V2__mwang-EXOWH_Wprime_M1400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_6iS.root',
 ] )