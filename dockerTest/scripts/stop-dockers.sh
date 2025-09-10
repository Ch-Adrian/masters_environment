#!/bin/bash

# Stop all running Docker containers

# Get list of running container IDs
running_containers=$(docker ps -q)

if [ -z "$running_containers" ]; then
    echo "No running containers found."
else
    echo "Stopping all running containers..."
    docker stop $running_containers
    echo "All containers stopped."
fi