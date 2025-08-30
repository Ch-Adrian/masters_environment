import docker
import time
import csv
import sys

client = docker.from_env()
container_jobmanager = client.containers.get("jobmanager")
container_taskmanager = client.containers.get("dockertest-taskmanager-1")

def main(task_name, mode, data_file):
    with open("../logs/metrics/metrics_"+task_name+"_"+mode+"_"+data_file+"_jobmanager"+".csv", "w") as f_jobmanager:
        writer_jobmanager = csv.writer(f_jobmanager)
        writer_jobmanager.writerow(["timestamp", "usage_MB", "limit_MB"])
        with open("../logs/metrics/metrics_"+task_name+"_"+mode+"_"+data_file+"_taskmanager"+".csv", "w") as f_taskmanager:
            writer_taskmanager = csv.writer(f_taskmanager)
            writer_taskmanager.writerow(["timestamp", "usage_MB", "limit_MB"])

            containers = [container_jobmanager, container_taskmanager]
            writers = [writer_jobmanager, writer_taskmanager]
            try:
                while True:
                    for idx, c in enumerate(containers):
                        stats = c.stats(stream=False)
                        usage = stats["memory_stats"]["usage"] / (1024*1024)
                        limit = stats["memory_stats"]["limit"] / (1024*1024)
                        writers[idx].writerow([time.time(), usage, limit])
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\nStopped tracking.")


if __name__ == "__main__":
    main(sys.argv[1].split("-1.3.0")[0], sys.argv[2], sys.argv[3].split(".")[0])