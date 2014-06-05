#!/bin/bash

####EDIT THIS PART#####

TREEDIR=/afs/cern.ch/work/m/mwang/public/EDBR/trees/productionv1_0416/ttbarcontrol/

##use 1 to resubmit, 0 not to resubmit
RESUB=0

QUEUE=8nh

##after everything is fine you can merge the output using MERGE=1
MERGE=1

##option for WW, to merege similar smaples using MERGESAMPLE=1. 
##NOTE: check the last part for safety
MERGESAMPLE=0

######################

eval `scram runtime -sh`


for sample in $(ls ${TREEDIR}/logs)
do
	#echo '##########################'
	#echo Checking $sample
	cd ${TREEDIR}/logs/${sample}
	cd   OutCmsBatch_*
	#loop over the jobs
	for job in $(ls |  grep Job)
	do
		#echo $job
		#check if there is a root file 
		cd $job
		if [ -f treeEDBR_${sample}.root ]
			then
			#echo Output file found!  
			#check the output log of this file
			log=LSFJOB_*/STDOUT
			egrep '1 fileAction           -s' -r $log &> /dev/null
			if [ $? != 0 ] 
            	then
				echo '##########################'
				echo Checking $sample
				echo $job
            	echo $log bad log! Please check the log.
				if test $RESUB -eq 1
					then
					echo Resubmit this job...
					rm -f treeEDBR_${sample}.root
					bsub -q $QUEUE -J "${sample}_${job}" batchScript.sh
				fi
        	#else 
        	   #echo good file!
        	fi
		else
			echo '##########################'
			echo Checking $sample
			echo $job
			echo Output root file not found!
			if test $RESUB -eq 1
				then
				echo Resubmit this job...
				bsub -q $QUEUE -J "${sample}_${job}" batchScript.sh
			fi 
		fi  ##end of if there is a root file
		cd ..
	done  ##end of loop over jobs

	#merge the outputs
	if test $MERGE -eq 1
		then
		echo merge the output of $sample
		cd ${TREEDIR}
		hadd treeEDBR_${sample}.root logs/${sample}/OutCmsBatch_*/Job_*/treeEDBR_${sample}.root
	fi
done  ##end of loop of sample



if test $MERGESAMPLE -eq 1
	then
	echo merging similar samples for plotting:
	cd ${TREEDIR}
	hadd treeEDBR_SingleTop_xwh.root treeEDBR_SingleTopBarSchannel_xwh.root treeEDBR_SingleTopBarTWchannel_xwh.root treeEDBR_SingleTopBarTchannel_xwh.root treeEDBR_SingleTopSchannel_xwh.root treeEDBR_SingleTopTWchannel_xwh.root treeEDBR_SingleTopTchannel_xwh.root
	hadd treeEDBR_VV_xwh.root treeEDBR_WW_xwh.root treeEDBR_WZ_xwh.root treeEDBR_ZZ_xwh.root
	hadd treeEDBR_DYJets_xwh.root treeEDBR_DYJetsPt*
	root -l -b -q $CMSSW_BASE/src/ExoDiBosonResonances/EDBRCommon/test/mergeDATA.C\(\"${TREEDIR}\"\)
	hadd treeEDBR_allBkg_xwh.root treeEDBR_DYJets_xwh.root treeEDBR_TTBARpowheg_xwh.root treeEDBR_VV_xwh.root treeEDBR_WJetsPt100_xwh.root treeEDBR_SingleTop_xwh.root
fi



