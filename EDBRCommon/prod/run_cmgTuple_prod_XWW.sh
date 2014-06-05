#! /bin/bash

SAMPLE_Run2012MU=( SingleMu_Run2012A-22Jan2013 SingleMu_Run2012B-22Jan2013 SingleMu_Run2012C-22Jan2013 SingleMu_Run2012D-22Jan2013  ) 
SAMPLE_Run2012ELE=( SingleElectron_Run2012A-22Jan2013 SingleElectron_Run2012B-22Jan2013 SingleElectron_Run2012C-22Jan2013 SingleElectron_Run2012D-22Jan2013   )

SAMPLE_MC1=( WJetsPt180 WJetsPt100 TTBARpowheg WW WZ ZZ  DYJetsPt100 SingleTopBarSchannel SingleTopBarTWchannel SingleTopBarTchannel SingleTopSchannel SingleTopTWchannel SingleTopTchannel ) # MC background 
SAMPLE_MC2=( MWp_270 MWp_270_bb MWp_270_cc MWp_270_gg MWp_300 MWp_300_bb MWp_300_cc MWp_300_gg MWp_350 MWp_350_bb MWp_350_cc MWp_350_gg MWp_400 MWp_400_bb MWp_400_cc MWp_400_gg MWp_450 MWp_450_bb MWp_450_cc MWp_450_gg MWp_500 MWp_500_bb MWp_500_cc MWp_500_gg MWp_550 MWp_550_bb MWp_550_cc MWp_550_gg MWp_600 MWp_600_bb MWp_600_cc MWp_600_gg MWp_650 MWp_650_bb MWp_650_cc MWp_650_gg MWp_700 MWp_700_bb MWp_700_cc MWp_700_gg MWp_750 MWp_750_bb MWp_750_cc MWp_750_gg MWp_800 MWp_800_bb MWp_800_cc MWp_800_gg MWp_900 MWp_900_bb MWp_900_cc MWp_900_gg MWp_1000 MWp_1000_bb MWp_1000_cc MWp_1000_gg MWp_1100 MWp_1100_bb MWp_1100_cc MWp_1100_gg MWp_1200 MWp_1200_bb MWp_1200_cc MWp_1200_gg MWp_1300 MWp_1300_bb MWp_1300_cc MWp_1300_gg MWp_1400 MWp_1400_bb MWp_1400_cc MWp_1400_gg MWp_1500 MWp_1500_bb MWp_1500_cc MWp_1500_gg MWp_1600 MWp_1600_bb MWp_1600_cc MWp_1600_gg MWp_1700 MWp_1700_bb MWp_1700_cc MWp_1700_gg MWp_1800 MWp_1800_bb MWp_1800_cc MWp_1800_gg MWp_1900 MWp_1900_bb MWp_1900_cc MWp_1900_gg MWp_2000 MWp_2000_bb MWp_2000_cc MWp_2000_gg MWp_2100 MWp_2100_bb MWp_2100_cc MWp_2100_gg MWp_2300 MWp_2300_bb MWp_2300_cc MWp_2300_gg MWp_2400 MWp_2400_bb MWp_2400_cc MWp_2400_gg MWp_2500 MWp_2500_bb MWp_2500_cc MWp_2500_gg MWp_2600 MWp_2600_bb MWp_2600_cc MWp_2600_gg MWp_2700 MWp_2700_bb MWp_2700_cc MWp_2700_gg MWp_2800 MWp_2800_bb MWp_2800_cc MWp_2800_gg MWp_2900 MWp_2900_bb MWp_2900_cc MWp_2900_gg MWp_3000 MWp_3000_bb MWp_3000_cc MWp_3000_gg ) #BulkG_WW_inclusive_c0p2_M600 BulkG_WW_inclusive_c0p2_M700 BulkG_WW_inclusive_c0p2_M800 BulkG_WW_inclusive_c0p2_M900 BulkG_WW_inclusive_c0p2_M1000 BulkG_WW_inclusive_c0p2_M1100 BulkG_WW_inclusive_c0p2_M1200 BulkG_WW_inclusive_c0p2_M1300 BulkG_WW_inclusive_c0p2_M1400 BulkG_WW_inclusive_c0p2_M1500 BulkG_WW_inclusive_c0p2_M1600 BulkG_WW_inclusive_c0p2_M1700 BulkG_WW_inclusive_c0p2_M1800 BulkG_WW_inclusive_c0p2_M1900 BulkG_WW_inclusive_c0p2_M2000 BulkG_WW_inclusive_c0p2_M2100 BulkG_WW_inclusive_c0p2_M2200 BulkG_WW_inclusive_c0p2_M2300 BulkG_WW_inclusive_c0p2_M2400 BulkG_WW_inclusive_c0p2_M2500 BulkG_WW_inclusive_M1000_W50 BulkG_WW_inclusive_M1000_W150 BulkG_WW_inclusive_M1000_W300 BulkG_WW_inclusive_M1500_W75 BulkG_WW_inclusive_M1500_W225 BulkG_WW_inclusive_M1500_W450 BulkG_WW_inclusive_M2100_W105 BulkG_WW_inclusive_M2100_W315 BulkG_WW_inclusive_M2100_W630 WprimeWZ_inclusive_M1000_PYTHIA6 WprimeWZ_inclusive_M1500_PYTHIA6 WprimeWZ_inclusive_M1800_PYTHIA6 WprimeWZ_inclusive_M2000_PYTHIA6 WprimeWZ_inclusive_M2200_PYTHIA6 WprimeWZ_inclusive_M2500_PYTHIA6 WprimeWZ_inclusive_M3000_PYTHIA6  WprimeWZ_inclusive_M4000_PYTHIA6 WprimeWZ_inclusive_M750_PYTHIA6 RSG_WW_lvjj_c0p05_M1000_PYTHIA6  RSG_WW_lvjj_c0p05_M1750_PYTHIA6 RSG_WW_lvjj_c0p05_M1250_PYTHIA6  RSG_WW_lvjj_c0p05_M2000_PYTHIA6 RSG_WW_lvjj_c0p05_M1500_PYTHIA6  RSG_WW_lvjj_c0p05_M750_PYTHIA6 )  # MC signal

OUTPATHBASE="/store/cmst3/group/exovv/CMGtuple/mwang/productionWH0412/"
OUTPATHDATA=${OUTPATHBASE}/Run2012/CA8/
OUTLOGPATHDATA=productionWH0412/Run2012/CA8/
OUTPATHMC=${OUTPATHBASE}/Summer12/CA8/
OUTLOGPATHMC=productionWH0412/Summer12/CA8/

cmsMkdir $OUTPATHMC
cmsMkdir $OUTPATHDATA

MYCMSSW_AREA=${CMSSW_BASE}/src
cd $MYCMSSW_AREA
eval `scram runtime -sh`
cd -


##############################
############# MC #############
##############################


sub_ind=0
for sample in "${SAMPLE_MC1[@]}"
  do

  LOGDIR=logs/${OUTLOGPATHMC}
  OUTDIR=${OUTPATHMC}/${sample}_xwh
  NFILES=50
#  cmsMkdir  $OUTDIR
  QUEUE="8nh"


#for MC
   ${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/prod/cmsBatch_EXOVV.py $NFILES XWW_main_cfg.py  --notagCVS -o ${LOGDIR}/${sample}_xwh -r ${OUTDIR} -b "bsub -q "${QUEUE}" -J "cmg${sample}" < batchScript.sh" -c "infile=summer12_${sample}_cff lepton=both selection=presel mcordata=MC"

   let sub_ind=$sub_ind +1

done


#-------------------------------------------

sub_ind=0
for sample in "${SAMPLE_MC2[@]}"
  do
  LOGDIR=logs/${OUTLOGPATHMC}
  OUTDIR=${OUTPATHMC}/${sample}_xwh
  QUEUE="8nh"
 # cmsMkdir  $OUTDIR


#for MC
   ${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/prod/cmsBatch_EXOVV.py 2  XWW_main_cfg.py  -o ${LOGDIR}/${sample}_xwh -r ${OUTDIR} --notagCVS -b "bsub -q "${QUEUE}" -J "cmg${sample}" < batchScript.sh" -c "infile=summer12_${sample}_cff lepton=both selection=presel mcordata=MC"
   let sub_ind=$sub_ind +1
done


################################
############# DATA #############
################################

sub_ind=0
for sample in "${SAMPLE_Run2012ELE[@]}"
  do
  LOGDIR=logs/${OUTLOGPATHDATA}
  OUTDIR=${OUTPATHDATA}/${sample}_xwh
  QUEUE="8nh"
 # cmsMkdir  $OUTDIR

  NFILES=50

  JSONFILE="dummy.json"
  if [[ "$sample" =~ "Photon" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  elif [[ "$sample" =~ "DoubleMu" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  elif [[ "$sample" =~ "SingleMu" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  elif [[ "$sample" =~ "SingleElectron" ]]
      then
	  JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  else
      echo "UNRECOGNIZED TYPE OF DATA SAMPLE ! "
      echo $sample
      echo"EXITING "
      exit 1
  fi

#for data
#  echo $JSONFILE
   ${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/prod/cmsBatch_EXOVV.py $NFILES XWW_main_cfg.py   -o ${LOGDIR}/${sample}_xwh -r ${OUTDIR} --notagCVS -b "bsub -q "${QUEUE}" -J "cmg${sample}" < batchScript.sh" -c "infile=data12_${sample}_cff lepton=both selection=presel mcordata=DATASE json=${JSONFILE}"

   let sub_ind=$sub_ind +1
done


#-------------------------------------------

sub_ind=0
for sample in "${SAMPLE_Run2012MU[@]}"
  do
  LOGDIR=logs/${OUTLOGPATHDATA}
  OUTDIR=${OUTPATHDATA}/${sample}_xwh
  QUEUE="8nh"
 # cmsMkdir  $OUTDIR
  JSONFILE="dummy.json"
  NFILES=50


  JSONFILE="dummy.json"
  if [[ "$sample" =~ "Photon" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  elif [[ "$sample" =~ "DoubleMu" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  elif [[ "$sample" =~ "SingleMu" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  elif [[ "$sample" =~ "SingleElectron" ]]
      then
      JSONFILE="${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/data/goldenAnalysisJSON.txt"
  else
      echo "UNRECOGNIZED TYPE OF DATA SAMPLE ! "
      echo $sample
      echo"EXITING "
      exit 1
  fi

#for MC
#  /afs/cern.ch/user/b/bonato/scratch0/PhysAnalysis/CMGTools/CMSSW_4_2_3/src/CMGTools/Common/scripts/cmsBatch2L2Q_MM2.py 15 HLLJJTemplateBoth_cff.py -o logs/${sample} -r ${OUTDIR} -b "bsub -q 1nd -J "cmg${sample}" < batchScript.sh" -c "infile=summer11_${sample}_cff lepton=both selection=full mcordata=MC"

#for data
###  echo $JSONFILE
  ${MYCMSSW_AREA}/ExoDiBosonResonances/EDBRCommon/prod/cmsBatch_EXOVV.py $NFILES XWW_main_cfg.py  -o ${LOGDIR}/${sample}_xwh -r ${OUTDIR} --notagCVS -b "bsub -q "${QUEUE}" -J "cmg${sample}" < batchScript.sh" -c "infile=data12_${sample}_cff lepton=both selection=presel mcordata=DATASM json=${JSONFILE}"  ##json=${JSONFILE}

   let sub_ind=$sub_ind +1

done
