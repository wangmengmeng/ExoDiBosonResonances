import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.helpers import *
process = cms.Process("EDBR")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string("START53_V23::All")
process.load("Configuration.StandardSequences.MagneticField_cff")


### input cmgTuples
#process.load("ExoDiBosonResonances.EDBRCommon.mwang_0120.cmgTuple_<SAMPLE>_cff")
process.load("ExoDiBosonResonances.EDBRCommon.mwang_0412.cmgTuple_<SAMPLE>_cff")
#CA8
#process.load("ExoDiBosonResonances.EDBRCommon.datasets.cmgTupleList_XWW.cmgTuple_08032013_CA8.cmgTuple_<SAMPLE>_cff")
#AK7
#process.load("ExoDiBosonResonances.EDBRCommon.datasets.cmgTupleList_XWW.cmgTuple_08032013_AK7.cmgTuple_<SAMPLE>_cff")
#
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))

## process.source = cms.Source("PoolSource",
##                     noEventSort = cms.untracked.bool(True),
##                     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
##                     fileNames = cms.untracked.vstring(
##     '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Summer12/presel/TTBAR/test_0.root')
##                     )

### it's useful to have the summary
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

from ExoDiBosonResonances.EDBRCommon.analyzerEDBR_cfi import AnalyzerXZZ
process.ANEDBR = AnalyzerXZZ.clone(
    debug=cms.bool(False),
    outFileName=cms.string("treeEDBR_<SAMPLE>.root"),
#comment and change for WH
#    VType=cms.string("W"),
    VType1=cms.string("W"),
    VType2=cms.string("H"),
    Ngen=cms.uint32(1),
    xsec=cms.double(1.0) ###in pb
    )

# comment this for WH
if "WW"=="<ANALYSIS>" :
    process.ANEDBR.VType1 = cms.string("W")
    process.ANEDBR.VType2 = cms.string("H")
else :
    process.ANEDBR.VType1 = cms.string("Z")
    process.ANEDBR.VType2 = cms.string("Z")


### if false, use the default collections
### in ExoDiBosonResonances.EDBRCommon.analyzerEDBR_cfi
### (i.e. all the cands passing pre-selection cuts)
processFullSel='<PROCESS>'

if processFullSel == "fullsb" :
    process.ANEDBR.EDBREEJJColl=cms.InputTag("BestSidebandSelectorEle:doubleJet")
    process.ANEDBR.EDBRMMJJColl=cms.InputTag("BestSidebandSelectorMu:doubleJet")
    process.ANEDBR.EDBREEJColl=cms.InputTag("BestSidebandSelectorEle:singleJet")
    process.ANEDBR.EDBRMMJColl=cms.InputTag("BestSidebandSelectorMu:singleJet")
elif processFullSel == "fullsig" :
    process.ANEDBR.EDBREEJJColl=cms.InputTag("BestCandSelectorEle:doubleJet")
    process.ANEDBR.EDBRMMJJColl=cms.InputTag("BestCandSelectorMu:doubleJet")
    process.ANEDBR.EDBREEJColl=cms.InputTag("BestCandSelectorEle:singleJet")
    process.ANEDBR.EDBRMMJColl=cms.InputTag("BestCandSelectorMu:singleJet")
elif processFullSel == "fullrange" :
    process.ANEDBR.EDBREEJJColl=cms.InputTag("BestFullRangeSelectorEle:doubleJet")
    process.ANEDBR.EDBRMMJJColl=cms.InputTag("BestFullRangeSelectorMu:doubleJet")
    process.ANEDBR.EDBREEJColl=cms.InputTag("BestFullRangeSelectorEle:singleJet")
    process.ANEDBR.EDBRMMJColl=cms.InputTag("BestFullRangeSelectorMu:singleJet")  
elif processFullSel == "ttbarcontrol" :
    process.ANEDBR.EDBREEJJColl=cms.InputTag("BestTTBarSelectorEle:doubleJet")
    process.ANEDBR.EDBRMMJJColl=cms.InputTag("BestTTBarSelectorMu:doubleJet")
    process.ANEDBR.EDBREEJColl=cms.InputTag("BestTTBarSelectorEle:singleJet")
    process.ANEDBR.EDBRMMJColl=cms.InputTag("BestTTBarSelectorMu:singleJet")
else :
    print 'Processing preselected collections (default)'


##### set Ngen and xsect values ofr MC samples; xsect in pb !!! 
if "TTBARpowheg"=="<SAMPLE>" or "TTBARpowheg_xwh"=="<SAMPLE>":
    process.ANEDBR.Ngen=cms.uint32(21675970)
    process.ANEDBR.xsec=cms.double(225.197)
elif "DYJetsPt100" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12511326)
    process.ANEDBR.xsec=cms.double(39.1) # 39.1 = 32.9 (from PREP) times 1.188
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "WW"=="<SAMPLE>" or "WW_xwh"=="<SAMPLE>":
    process.ANEDBR.Ngen=cms.uint32(10000431)
    process.ANEDBR.xsec=cms.double(57.1097)
elif "WZ"=="<SAMPLE>" or "WZ_xwh"=="<SAMPLE>":
    process.ANEDBR.Ngen=cms.uint32(10000283)
    process.ANEDBR.xsec=cms.double(33.21)
elif "ZZ"=="<SAMPLE>" or "ZZ_xwh"=="<SAMPLE>":
    process.ANEDBR.Ngen=cms.uint32(9799908)
    process.ANEDBR.xsec=cms.double(8.059)
    process.ANEDBR.FillGenLevelCode=cms.uint32(3)
elif "WJetsPt100" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12742382)
    process.ANEDBR.xsec=cms.double(282.5)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "WJetsPt180" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(9737030)
    process.ANEDBR.xsec=cms.double(29.00)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "SingleTopBarSchannel" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(139974)
    process.ANEDBR.xsec=cms.double(1.76)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "SingleTopBarTWchannel" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(493460)
    process.ANEDBR.xsec=cms.double(11.1)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "SingleTopBarTchannel" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(1935072)
    process.ANEDBR.xsec=cms.double(30.7)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)    
elif "SingleTopSchannel" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(259961)
    process.ANEDBR.xsec=cms.double(3.79)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)    
elif "SingleTopTWchannel" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(497658)
    process.ANEDBR.xsec=cms.double(11.1)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)    
elif "SingleTopTchannel" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(3758227)
    process.ANEDBR.xsec=cms.double(56.4)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)    
### MC signal
## add for WH MC signal smaples
elif "MWp_270_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19596)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_270_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(11997)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_270_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(527)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_270_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(7071)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_300_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(18002)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_300_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(11060)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_300_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(505)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_300_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6435)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_350_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19999)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_350_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12603)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_350_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(552)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_350_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6842)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_400_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19599)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_400_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(2404)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_400_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(553)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_400_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6641)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_450_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19600)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_450_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12658)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_450_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(548)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_450_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6392)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_500_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19198)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_500_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(2471)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_500_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(561)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_500_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6165)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_550_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19997)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_550_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13169)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_550_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(592)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_550_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6235)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_600_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(20000)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_600_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13195)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_600_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(524)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_600_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6259)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_650_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19998)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_650_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13015)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_650_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(536)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_650_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5911)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_700_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19999)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_700_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13348)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_700_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(613)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_700_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(6036)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_750_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19599)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_750_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13127)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_750_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(567)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_750_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5904)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_800_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19600)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_800_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13191)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_800_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(563)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_800_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5844)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_900_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19999)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_900_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13509)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_900_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(619)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_900_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5179)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1000_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12687-497) ## subtract 497 because one job didn't in cmg output
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1000_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(8561)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1000_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(399)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1000_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(3725)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1100_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(18815)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1100_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12702)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1100_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(589)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1100_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5413)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1200_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19998)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1200_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13592)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1200_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(630)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1200_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5774)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1300_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19997)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1300_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13657)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1300_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(664)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1300_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5674)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1400_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19999)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1400_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13733)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1400_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(661)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1400_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5590)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1500_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19600)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1500_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13436)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1500_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(616)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1500_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5546)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1600_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19997)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1600_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13758)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1600_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(657)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1600_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5580)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1700_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19201)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1700_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13225)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1700_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(653)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1700_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5321)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1800_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(14516)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1800_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(10089)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1800_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(467)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1800_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(3959)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1900_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19995)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1900_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13836)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1900_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(690)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_1900_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5467)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2000_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19152)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2000_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13302)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2000_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(638)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2000_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5211)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2100_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19606)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2100_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13976)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2100_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(647)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2100_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5374)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2300_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(17200)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2300_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(12054)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2300_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(600)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2300_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(4545)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2400_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19600)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2400_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13715)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2400_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(684)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2400_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5200)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2500_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19213)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2500_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(114104)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2500_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(643)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2500_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(5005)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2600_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(14412)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2600_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(10111)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2600_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(513)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2600_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(3712)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2700_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19998)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2700_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(14079)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2700_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(638)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2700_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(4932)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2800_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(18401)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2800_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13000)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2800_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(604)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2800_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(4784)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2900_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(19201)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2900_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13576)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2900_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(572)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_2900_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(4990)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_3000_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(13600)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_3000_bb_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(9632)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_3000_cc_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(465)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "MWp_3000_gg_xwh" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(3502)
    process.ANEDBR.xsec=cms.double(1) ### Checked
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
#elif "BulkG_WW_lvjj_c0p2_M23000" in "<SAMPLE>" :
#    process.ANEDBR.Ngen=cms.uint32(9898) ### Checked
#    process.ANEDBR.xsec=cms.double(2.5515e-07)
#    process.ANEDBR.FillGenLevelCode=cms.uint32(7)

#ww (new, used for PAPER)
# ww signal (exclusive W-->l v decays, despite of the name, since we use pattuples filtered at gen level) 
#elif "BulkG_WW_inclusive_c0p2_M3000_xww" in "<SAMPLE>" :
#    process.ANEDBR.Ngen=cms.uint32(11854) ### Checked
#    process.ANEDBR.xsec=cms.double(2.292e-02)
#    process.ANEDBR.FillGenLevelCode=cms.uint32(7)

###### W' => WZ, PYTHIA 6, inclusive
#elif "<SAMPLE>"  == "WprimeWZ_inclusive_M3000_PYTHIA6"  :
#    process.ANEDBR.Ngen=cms.uint32(300000)
#    process.ANEDBR.xsec=cms.double(0.727785)
#    process.ANEDBR.FillGenLevelCode=cms.uint32(7)

### Data
#zz--doublemu
elif "<SAMPLE>"=="DoubleMu_Run2012A_22Jan2013" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "DoubleMuParked_Run2012" in "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
##zz--doubleEle
elif "<SAMPLE>"=="Photon_Run2012A_22Jan2013" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "DoublePhotonHighPt_Run2012" in  "<SAMPLE>" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
#ww--singlemu
elif "<SAMPLE>"=="SingleMu_Run2012A_13Jul2012_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012A_recover_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012B_13Jul2012_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012C_24Aug2012_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012C_PromptReco_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012C_EcalRecove_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012D_PromptReco_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
#ww---singleEle
elif "<SAMPLE>"=="SingleElectron_Run2012A_13Jul2012_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)  
elif "<SAMPLE>"=="SingleElectron_Run2012A_recover_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)   
elif "<SAMPLE>"=="SingleElectron_Run2012B_13Jul2012_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012C_24Aug2012_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012C_PromptReco_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012C_EcalRecove_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012D_PromptReco_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
   
#for 539
#single mu
elif "<SAMPLE>"=="SingleMu_Run2012A-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012B-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012C-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleMu_Run2012D-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
#single ele
elif "<SAMPLE>"=="SingleElectron_Run2012A-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012B-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012C-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="SingleElectron_Run2012D-22Jan2013_xwh" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)

else :
    print 'ERROR !!! Sample named <SAMPLE> was not recognized !'

print '---> Ngen=',process.ANEDBR.Ngen,'  Xsect=',process.ANEDBR.xsec

## no need for wh
###apply V-tagging scale factor only to signal MC samples
#if "BulkG_ZZ_lljj_" in "<SAMPLE>" or "RSG_ZZ_lljj_" in "<SAMPLE>" or "WprimeWZ_" in "<SAMPLE>" or "WW"=="<SAMPLE>" or "WZ"=="<SAMPLE>" or "ZZ"=="<SAMPLE>":
#       process.ANEDBR.VTaggingScaleFactorHP=cms.double(0.891)
#       process.ANEDBR.VTaggingScaleFactorLP=cms.double(1.277)


       
#if "BulkG_WW_inclusive_" in "<SAMPLE>" or "RSG_WW_lvjj_" in "<SAMPLE>"  or "WprimeWZ_" in "<SAMPLE>" or "WW_xww"=="<SAMPLE>" or "WZ_xww"=="<SAMPLE>" or "ZZ_xww"=="<SAMPLE>":
#       process.ANEDBR.VTaggingScaleFactorHP=cms.double(0.891)
#       process.ANEDBR.VTaggingScaleFactorLP=cms.double(1.277)

process.filterFinalSelPath = cms.EDFilter("HLTHighLevel",
                                          TriggerResultsTag = cms.InputTag("TriggerResults","","CMG"),
                                          HLTPaths = cms.vstring("FullPathDUMMYELE","FullPathDUMMYMU"),
                                          #HLTPaths = cms.vstring("cmgEDBRZZEle","cmgEDBRZZMu"),
                                          eventSetupPathsKey = cms.string(''),
                                          andOr = cms.bool(True),  # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                          throw = cms.bool(True)    # throw exception on unknown path names
                                          )

if "WW"=="<ANALYSIS>" :
    process.filterFinalSelPath.HLTPaths = cms.vstring("cmgEDBRWWEle","cmgEDBRWWMu")
else :
    process.filterFinalSelPath.HLTPaths = cms.vstring("cmgEDBRZZEle","cmgEDBRZZMu")
        

#AB: should we add also "ttbarcontrol" ? LS: yes
if processFullSel=="fullsb" or processFullSel=="fullsig" or processFullSel=="fullrange" or processFullSel=="ttbarcontrol":
    process.p=cms.Path(process.filterFinalSelPath+process.ANEDBR)
else :
    process.p=cms.Path(process.ANEDBR)
