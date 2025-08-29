#!/bin/bash

done="\e[32mDONE\e[0m"

echo -n "Clean-up..."
touch ../logs/app.log
touch ../logs/runner.log
touch ../logs/output.log
echo -e $done

echo -n "Cleaning topics..."
docker exec dockertest-kafka-1-1 sh -c "/bin/kafka-topics --bootstrap-server kafka-1:9092 --delete --topic input"
docker exec dockertest-kafka-1-1 sh -c "/bin/kafka-topics --bootstrap-server kafka-1:9092 --delete --topic output"
docker exec dockertest-kafka-1-1 sh -c "/bin/kafka-topics --bootstrap-server kafka-1:9092 --delete --topic metrics"
echo -e $done

echo -n "Sleeping..."
sleep 5
echo -e $done

echo "Creating topics..."
docker exec dockertest-kafka-1-1 sh -c "/bin/kafka-topics --bootstrap-server kafka-1:9092 --create --topic input   --replication-factor 1 --partitions 1"
docker exec dockertest-kafka-1-1 sh -c "/bin/kafka-topics --bootstrap-server kafka-1:9092 --create --topic output  --replication-factor 1 --partitions 1"
docker exec dockertest-kafka-1-1 sh -c "/bin/kafka-topics --bootstrap-server kafka-1:9092 --create --topic metrics --replication-factor 1 --partitions 1"
echo -e $done

echo "Fill topic 'input' with inc-dec setting..."
java -jar ../jars/data-loader.jar $2 $4 &> ../logs/runner.log
echo -e $done

#if [[ "$2" == "true" ]]; then
#  echo -e "Incremental fill:"
#  java -jar ../jars/Kafka2-input-filler-with-email.jar &> ../logs/runner.log
#else
#  echo -e "Decremental fill:"
#  java -jar ../jars/Kafka2-input-filler-with-email-inc-dec.jar &> ../logs/runner.log
#fi
#java -jar ../jars/Kafka2-input-filler.jar &> ../logs/runner.log
#java -jar ../jars/Kafka2-input-filler-with-email.jar &> ../logs/runner.log
#echo -e $done

#echo "Copying jar file..."
#./copy_jars.sh
#echo -e $done

echo -n "Testing app: $1 ..."
./run_job.sh $1 $2 $3 >> ../logs/runner.log 2>&1 &
echo -e $done

echo -n "Sleeping..."
sleep 2
echo -e $done

echo $(grep -o "JobID [a-fA-F0-9]\+" ../logs/runner.log | awk '{print $2}' | head -1)

#./show_output.sh &> ../logs/output.log &
#./show_metrics.sh &> ../logs/metrics.log &

echo "Start scanning metrics topic..."
java -jar ../jars/data-scanner.jar &
echo -e $done

echo -n "Sleeping..."
sleep 120
echo -e $done

jobID=$(grep -o "JobID [a-fA-F0-9]\+" ../logs/runner.log | awk '{print $2}' | head -1)
echo "Stopping job: $jobID..."
./stop_job.sh $jobID
echo -e $done

echo "Killing metrics scanner: metrics_scanner_PID..."
ps -ef | grep "java -jar ../jars/Kafka2-metrics-scanner.jar" | head -1 | awk '{print $2}' | xargs kill
echo -e $done

echo "Plotting image..."
/usr/bin/python plotMetrics.py $1 $2 $4
echo -e $done