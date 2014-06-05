import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_N9I.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_rwE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_Ai5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_Awg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_Sb4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_aFM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_Sym.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_WPC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_IMQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_wqL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_X1R.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_skX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_XFb.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_itx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_Q3i.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_Ysz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_jD9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_7HT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_SsS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_GVA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_lrZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_2JB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_ckX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_90E.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_vR9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_lJf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_3bF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_BlO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_2bx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_QFJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_Jce.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_RIT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_mg0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_1yy.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_kzp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_cyt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_eRu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_xeS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_36a.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_XGS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_I8b.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_r6x.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_mhS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_jPd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_EY6.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_jFa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_1Gn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_PMH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_CHn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2400_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2400_GENSIM_V2__mwang-EXOWH_Wprime_M2400_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_vt9.root',
 ] )
