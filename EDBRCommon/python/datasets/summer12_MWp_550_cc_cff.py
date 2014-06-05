import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_3_zMR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_3_Fdi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_3_Tht.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_3_ptK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_3_OW4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_3_kFE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_3_5Xe.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_3_cnc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_3_tbC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_3_YBh.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_3_B1v.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_3_oau.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_3_r3X.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_3_UJZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_3_6lr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_3_9hm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_3_wtq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_3_otZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_3_mom.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_3_DgY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_3_5Kc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_3_Sdm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_3_3X2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_3_caG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_3_GSU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_3_Jtx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_3_2qG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_3_ufM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_3_1Tr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_3_0cJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_3_MTm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_3_nEz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_3_uJE.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_3_WQu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_3_2pQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_3_7f2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_3_TYR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_3_J49.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_3_bmm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_3_QCf.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_3_Iod.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_3_WUL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_3_Q8c.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_3_600.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_3_SuM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_3_PHR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_3_E9w.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_3_z62.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_2_0Eo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_3_Jhj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M550_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M550_GENSIM_V2__mwang-EXOWH_Wprime_M550_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_3_pzm.root',
 ] )