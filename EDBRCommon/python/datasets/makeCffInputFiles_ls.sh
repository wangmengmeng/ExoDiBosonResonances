#!/bin/sh

### Output directory for the lists ###

OUTPUTDIR=$USER
mkdir -p $OUTPUTDIR

### Location of CMGtuples ###

MAINDIRMC=/store/cmst3/group/exovv/CMGtuple/mwang/productionWH0412/Summer12/CA8
MAINDIRDATA=/store/cmst3/group/exovv/CMGtuple/mwang/productionWH0412/Run2012/CA8

### Make lists for DATA ###

for sample in SingleElectron_Run2012A-22Jan2013_xwh SingleElectron_Run2012B-22Jan2013_xwh SingleElectron_Run2012C-22Jan2013_xwh SingleElectron_Run2012D-22Jan2013_xwh SingleMu_Run2012A-22Jan2013_xwh SingleMu_Run2012B-22Jan2013_xwh SingleMu_Run2012C-22Jan2013_xwh SingleMu_Run2012D-22Jan2013_xwh
do
  echo $MAINDIRDATA/$sample
  cmsLs $MAINDIRDATA/$sample | grep .root | awk '{print $5}'  > tmp.txt
  python makeCffInputFiles_ls.py tmp.txt $OUTPUTDIR/cmgTuple_${sample}_cff.py
done

### Make lists for MC ###

for sample in WJetsPt180_xwh WJetsPt100_xwh TTBARpowheg_xwh WW_xwh WZ_xwh ZZ_xwh  DYJetsPt100_xwh SingleTopBarSchannel_xwh SingleTopBarTWchannel_xwh SingleTopBarTchannel_xwh SingleTopSchannel_xwh SingleTopTWchannel_xwh SingleTopTchannel_xwh MWp_270_xwh MWp_270_bb_xwh MWp_270_cc_xwh MWp_270_gg_xwh MWp_300_xwh MWp_300_bb_xwh MWp_300_cc_xwh MWp_300_gg_xwh MWp_350_xwh MWp_350_bb_xwh MWp_350_cc_xwh MWp_350_gg_xwh MWp_400_xwh MWp_400_bb_xwh MWp_400_cc_xwh MWp_400_gg_xwh MWp_450_xwh MWp_450_bb_xwh MWp_450_cc_xwh MWp_450_gg_xwh MWp_500_xwh MWp_500_bb_xwh MWp_500_cc_xwh MWp_500_gg_xwh MWp_550_xwh MWp_550_bb_xwh MWp_550_cc_xwh MWp_550_gg_xwh MWp_600_xwh MWp_600_bb_xwh MWp_600_cc_xwh MWp_600_gg_xwh MWp_650_xwh MWp_650_bb_xwh MWp_650_cc_xwh MWp_650_gg_xwh MWp_700_xwh MWp_700_bb_xwh MWp_700_cc_xwh MWp_700_gg_xwh MWp_750_xwh MWp_750_bb_xwh MWp_750_cc_xwh MWp_750_gg_xwh MWp_800_xwh MWp_800_bb_xwh MWp_800_cc_xwh MWp_800_gg_xwh MWp_900_xwh MWp_900_bb_xwh MWp_900_cc_xwh MWp_900_gg_xwh MWp_1000_xwh MWp_1000_bb_xwh MWp_1000_cc_xwh MWp_1000_gg_xwh MWp_1100_xwh MWp_1100_bb_xwh MWp_1100_cc_xwh MWp_1100_gg_xwh MWp_1200_xwh MWp_1200_bb_xwh MWp_1200_cc_xwh MWp_1200_gg_xwh MWp_1300_xwh MWp_1300_bb_xwh MWp_1300_cc_xwh MWp_1300_gg_xwh MWp_1400_xwh MWp_1400_bb_xwh MWp_1400_cc_xwh MWp_1400_gg_xwh MWp_1500_xwh MWp_1500_bb_xwh MWp_1500_cc_xwh MWp_1500_gg_xwh MWp_1600_xwh MWp_1600_bb_xwh MWp_1600_cc_xwh MWp_1600_gg_xwh MWp_1700_xwh MWp_1700_bb_xwh MWp_1700_cc_xwh MWp_1700_gg_xwh MWp_1800_xwh MWp_1800_bb_xwh MWp_1800_cc_xwh MWp_1800_gg_xwh MWp_1900_xwh MWp_1900_bb_xwh MWp_1900_cc_xwh MWp_1900_gg_xwh MWp_2000_xwh MWp_2000_bb_xwh MWp_2000_cc_xwh MWp_2000_gg_xwh MWp_2100_xwh MWp_2100_bb_xwh MWp_2100_cc_xwh MWp_2100_gg_xwh MWp_2300_xwh MWp_2300_bb_xwh MWp_2300_cc_xwh MWp_2300_gg_xwh MWp_2400_xwh MWp_2400_bb_xwh MWp_2400_cc_xwh MWp_2400_gg_xwh MWp_2500_xwh MWp_2500_bb_xwh MWp_2500_cc_xwh MWp_2500_gg_xwh MWp_2600_xwh MWp_2600_bb_xwh MWp_2600_cc_xwh MWp_2600_gg_xwh MWp_2700_xwh MWp_2700_bb_xwh MWp_2700_cc_xwh MWp_2700_gg_xwh MWp_2800_xwh MWp_2800_bb_xwh MWp_2800_cc_xwh MWp_2800_gg_xwh MWp_2900_xwh MWp_2900_bb_xwh MWp_2900_cc_xwh MWp_2900_gg_xwh MWp_3000_xwh MWp_3000_bb_xwh MWp_3000_cc_xwh MWp_3000_gg_xwh

do
  echo $MAINDIRMC/$sample
  cmsLs $MAINDIRMC/$sample | grep .root | awk '{print $5}'  > tmp.txt
  python makeCffInputFiles_ls.py tmp.txt $OUTPUTDIR/cmgTuple_${sample}_cff.py
done

### Remove tmp file ###

rm -f tmp.txt
