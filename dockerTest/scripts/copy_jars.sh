#!/bin/bash

echo -n "Cleaning and building project algorithms..."
rm -rf ../workspace/tasks/*
#PTH=/home/adrian/dev/masters_environment/dockerTest/logs
#(cd /home/adrian/dev/algorithms && ( ( mvn clean package ) 2>&1 | tee $PTH/app.log ) )
(cd /home/adrian/dev/algorithms && ( ( mvn clean package ) &> /home/adrian/dev/masters_environment/dockerTest/logs/app.log ) )
echo " DONE"

echo -n "Sleeping..."
sleep 3
echo " DONE"

echo -n "Copying jars..."
cp /home/adrian/dev/algorithms/dynamic-connectivity-incremental/target/dynamic-connectivity-incremental-1.3.0.jar ../workspace/tasks/dynamic-connectivity-incremental-1.3.0.jar
cp /home/adrian/dev/algorithms/dynamic-connectivity-ett/target/dynamic-connectivity-ett-1.3.0.jar ../workspace/tasks/dynamic-connectivity-ett-1.3.0.jar
cp /home/adrian/dev/algorithms/dynamic-connectivity-lct/target/dynamic-connectivity-lct-1.3.0.jar ../workspace/tasks/dynamic-connectivity-lct-1.3.0.jar
cp /home/adrian/dev/algorithms/dynamic-mst-ett-decremental/target/dynamic-mst-ett-decremental-1.3.0.jar ../workspace/tasks/dynamic-mst-ett-decremental-1.3.0.jar
cp /home/adrian/dev/algorithms/dynamic-sssp-decremental/target/dynamic-sssp-decremental-1.3.0.jar ../workspace/tasks/dynamic-sssp-decremental-1.3.0.jar
echo " DONE"

echo -n "Sleeping..."
sleep 10
echo " DONE"

echo "Operation completed."