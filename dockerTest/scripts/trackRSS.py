import psutil
import time
import csv
import sys

if len(sys.argv) < 3:
    print("Usage: python track_mem.py <PID> <output_file>")
    sys.exit(1)

pid = int(sys.argv[1])
outfile = sys.argv[2]

process = psutil.Process(pid)

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "rss_MB", "vms_MB"])

    try:
        while process.is_running():
            mem = process.memory_info()
            writer.writerow([time.time(), mem.rss / (1024*1024), mem.vms / (1024*1024)])
            time.sleep(1)
    except psutil.NoSuchProcess:
        print("Process ended.")
