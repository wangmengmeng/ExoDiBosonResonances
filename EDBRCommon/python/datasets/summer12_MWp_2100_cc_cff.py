import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_bCz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_J36.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_IZa.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_R3f.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_neX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_ldc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_pqk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_QSv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_Tgl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_6EC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_lZJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_tas.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_rIg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_1J7.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_Aap.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_8rw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_vyd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_GSk.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_HpY.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_rki.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_y2W.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_vAI.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_8ib.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_eGt.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_AQv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_62R.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_nIH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_TUx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_hRi.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_58P.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_RJx.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_5Co.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_Aoo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_A06.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_MiG.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_zfN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_XQ1.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_OVn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_C5U.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_NdN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_w6Y.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_reD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_7KN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_XB9.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_dqj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_qBX.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_lIT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_wpu.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_tt3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_E4e.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_cc_20140213_153653/mwang/EXOWH_Wprime_M2100_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/16c05133267617cea34f802d9c2b1826/EXOWH_Wprime_M2100_GENSIM_V2__mwang-EXOWH_Wprime_M2100_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_DMz.root',
 ] )
