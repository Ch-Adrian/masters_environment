#!/bin/bash
#
#jobID=$(grep -o "JobID [a-fA-F0-9]\+" ../logs/runner.log | awk '{print $2}' | head -1)
#echo "Stopping job: $jobID..."
#./stop_job.sh $jobID
#echo -e $done
#
#echo "Start scanning metrics topic..."
#java -jar ../jars/data-scanner.jar
#echo -e $done
#
#echo "Plotting image..."
#/usr/bin/python plotMetrics.py $1 $2 $4
#echo -e $done