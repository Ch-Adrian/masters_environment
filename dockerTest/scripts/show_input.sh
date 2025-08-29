#!/bin/bash

#echo "showing input..."
docker exec -i dockertest-kafka-2-1 sh -c "/bin/kafka-console-consumer --bootstrap-server kafka-1:9092 --topic input --from-beginning"