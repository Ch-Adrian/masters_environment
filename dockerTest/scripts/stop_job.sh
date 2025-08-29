#!/bin/bash

#bash /opt/flink/bin/flink cancel $1
#bash /opt/flink/bin/flink stop --savepointPath /tmp/flink-savepoints $1
docker exec -it jobmanager sh -c "/opt/flink/bin/flink stop --savepointPath /tmp/flink-savepoints $1"