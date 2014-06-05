import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_fpx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_hud.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_A3Z.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_JRp.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_4ai.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_1qG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_NXB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_WF0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_Bnf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_2iS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_Nr0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_CQK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_VuR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_7ei.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_u5L.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_sCv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_PeI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_px8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_lQz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_lDn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_MUB.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_gSj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_YLG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_LaF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_0gj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_SEP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_dsc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_B9U.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_wEC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_gck.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_ANc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_GOv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_pUc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_tVg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_nUm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_vD8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_7j7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_2iU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_ac0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_WOJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_r77.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_LQH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_eP9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_YTk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_rBN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_nYr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_84b.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_5PN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_qJ2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_yeD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M1200_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M1200_GENSIM_V2__mwang-EXOWH_Wprime_M1200_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_BFb.root',
 ] )
