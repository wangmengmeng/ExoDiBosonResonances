import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([

      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_10_1_4mP.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_11_1_9fq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_12_1_22e.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_13_1_PeJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_14_1_2M8.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_15_1_dYF.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_16_1_v6Z.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_17_1_1Up.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_18_1_nNM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_19_1_QrC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_1_1_kcA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_20_1_mSR.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_21_1_Y9e.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_22_1_CBn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_23_1_PPn.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_24_1_Pin.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_25_1_qCq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_26_1_STA.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_27_1_eEj.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_28_1_1oq.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_29_1_Evo.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_2_1_k5l.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_30_1_808.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_31_1_Jvd.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_32_1_zaL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_33_1_XWH.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_34_1_n2u.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_35_1_F83.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_36_1_EQO.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_37_1_pTL.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_38_1_j7E.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_39_1_Cvv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_3_1_73X.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_40_1_joM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_41_1_JX5.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_42_1_D21.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_43_1_3Zz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_44_1_fjS.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_45_1_ZYz.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_46_1_3dJ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_47_1_RO0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_48_1_nI2.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_49_1_7an.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_4_1_kEv.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_50_1_uGm.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_51_1_WgQ.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_5_1_lbM.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_6_1_K87.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_7_1_lJ0.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_8_1_bDC.root',
      '/store/cmst3/group/exovv/mwang/EDBR_PATtuple_edbr_wh_20140210_Summer12MC_WprimeWH_20140213_153624/mwang/EXOWH_Wprime_M2800_GENSIM_V2/EDBR_PATtuple_edbr_wh_20140210/6dd5c34efa97fc5295a711db48f1622c/EXOWH_Wprime_M2800_GENSIM_V2__mwang-EXOWH_Wprime_M2800_AODSIM_V2-2c74483358b1f8805e5601fc325d256c__USER_9_1_9eb.root',
 ] )