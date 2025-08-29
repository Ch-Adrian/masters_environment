#!/bin/bash

#bash /opt/flink/bin/flink run ../tasks/dynamic-connectivity-incremental-1.3.0.jar --port 9001 --bootstrap-server kafka-12:9092 --input-topic "input" --output-topic "output" --metrics-topic "metrics"
#docker exec -it jobmanager sh -c "/opt/flink/bin/flink run ./tasks/dynamic-connectivity-incremental-1.3.0.jar --port 9001 --bootstrap-server kafka-12:9092 --input-topic 'input' --output-topic 'output' --metrics-topic 'metrics'"
docker exec -i jobmanager sh -c "/opt/flink/bin/flink run ./tasks/$1 --port 9001 --bootstrap-server kafka-1:9092 --input-topic 'input' --output-topic 'output' --metrics-topic 'metrics' --algorithm-mode '$2' --amt-of-edges $3"
