#!/bin/bash

ZOOKEEPER=zookeeper-12
KAFKA12=kafka-12
KAFKA22=kafka-22
JOBMANAGER=jobmanager
TASKMANAGER=taskmanager

echo $ZOOKEEPER

bash -c "docker-compose start $ZOOKEEPER"

function checkContainerStatus () {
  if [ -z "$(docker-compose ps -q "$1")" ] || [ -z "$(docker ps -q --no-trunc | grep "$(docker-compose ps -q "$1")")" ]; then
    echo ""
  else
    echo "1"
  fi
}

result=$(checkContainerStatus $ZOOKEEPER)
sleep 10s

echo $?

docker-compose run -d --name dockertest-kafka-12-1 $KAFKA12

echo 'starts sleeping...'
sleep 15s
echo 'awaken...'

resultKafka12=$(checkContainerStatus $KAFKA12)
echo $resultKafka12
if [ -n "$resultKafka12" ]; then
    echo "kafka has stopped"
else
  echo "kafka is running"
fi

