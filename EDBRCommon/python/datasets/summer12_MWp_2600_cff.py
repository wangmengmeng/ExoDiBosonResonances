import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([

      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_T0f.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_QeT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_nMV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_ume.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_lZS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_WmO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_6Rv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_h3P.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_tc4.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_Rvq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_uQl.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_KKg.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_lWA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_GFw.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_K0c.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_bMj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_HFh.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_pet.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_e2O.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_ed0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_xLJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_odc.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_h4C.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_4US.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_jJU.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_PVV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_ZX8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_Kk2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_WZQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_mSV.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_6DK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_ceD.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_iK8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_YRv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_EAT.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_Z2v.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_6B3.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_Nqr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_fOM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_Ki2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_p9n.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_gcv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_fab.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_HiZ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_DTR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_RLN.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_9Yr.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_2aK.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_q7B.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_SyF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2600_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2600_GENSIM_V2__mwang-EXOWH_Wprime_M2600_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_t9S.root',
 ] )