#!/bin/bash

#bash /opt/flink/bin/stop-cluster.sh
docker exec -it jobmanager sh -c "/opt/flink/bin/stop-cluster.sh"
