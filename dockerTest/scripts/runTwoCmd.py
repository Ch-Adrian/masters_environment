import subprocess
import time
import signal
from kafka import KafkaConsumer, TopicPartition, errors
import re
from plotMetrics import plot_metrics
from kafka.admin import KafkaAdminClient, NewTopic

commands = {
    "web-NotreDame.txt": {
        "dynamic-connectivity-ett-1.3.0.jar": [0, 1, 2],
        "dynamic-connectivity-lct-1.3.0.jar": [0, 1, 2],
        "dynamic-connectivity-incremental-1.3.0.jar": [0],
        "dynamic-mst-ett-decremental-1.3.0.jar": [1],
        "dynamic-sssp-decremental-1.3.0.jar": [1],
    },
    "Email-EuAll.txt": {
        "dynamic-connectivity-ett-1.3.0.jar": [0, 1, 2],
        "dynamic-connectivity-lct-1.3.0.jar": [0, 1, 2],
        "dynamic-connectivity-incremental-1.3.0.jar": [0],
        "dynamic-mst-ett-decremental-1.3.0.jar": [1],
        "dynamic-sssp-decremental-1.3.0.jar": [1],
    },
    "facebook_combined.txt": {
        "dynamic-connectivity-ett-1.3.0.jar": [0, 1, 2],
        "dynamic-connectivity-lct-1.3.0.jar": [0, 1, 2],
        "dynamic-connectivity-incremental-1.3.0.jar": [0],
        "dynamic-mst-ett-decremental-1.3.0.jar": [1],
        "dynamic-sssp-decremental-1.3.0.jar": [1],
    }
}

commands2 = {
    "web-NotreDame.txt": {
        0: [
            "dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar",
            "dynamic-connectivity-incremental-1.3.0.jar"
        ],
        1: [
            "dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar",
            "dynamic-mst-ett-decremental-1.3.0.jar",
            "dynamic-sssp-decremental-1.3.0.jar"
        ],
        2: [
            "dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar"
        ]
    },
    "Email-EuAll.txt": {
        0: ["dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar",
            "dynamic-connectivity-incremental-1.3.0.jar"],
        1: ["dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar",
            "dynamic-mst-ett-decremental-1.3.0.jar",
            "dynamic-sssp-decremental-1.3.0.jar"],
        2: ["dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar"]
    },
    "facebook_combined.txt": {
        0: ["dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar",
            "dynamic-connectivity-incremental-1.3.0.jar"],
        1: ["dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar",
            "dynamic-mst-ett-decremental-1.3.0.jar",
            "dynamic-sssp-decremental-1.3.0.jar"],
        2: ["dynamic-connectivity-ett-1.3.0.jar",
            "dynamic-connectivity-lct-1.3.0.jar"]
    }
}

data_len = {
    "web-NotreDame.txt": [1497134, 2*1497134, 149713],
    "Email-EuAll.txt": [420045, 2*420045, 42004],
    "facebook_combined.txt": [88234, 2*88234, 8823]
}

BROKER = 'localhost:19092'
TOPICS = ['input', 'metrics', 'output']

def clean_files():
    with open("../logs/runner.log", "w") as f:
        f.write("")
    with open("../logs/app.log", "w") as f:
        f.write("")
    with open("../logs/output.log", "w") as f:
        f.write("")

def clean_topics(broker, topics):
    admin = KafkaAdminClient(bootstrap_servers=broker)
    admin.delete_topics(topics)
    admin.close()

def topic_exists(broker, topic):
    consumer = KafkaConsumer(bootstrap_servers=broker)
    exists = topic in consumer.topics()
    consumer.close()
    # print(f"Topic '{topic}' exists: {exists}")
    return exists

def create_topics(broker, topics):
    admin = KafkaAdminClient(bootstrap_servers=broker)
    new_topics = [NewTopic(name=topic, num_partitions=1, replication_factor=1) for topic in topics]
    admin.create_topics(new_topics=new_topics, validate_only=False)
    admin.close()

def manage_topic(broker, topic):
    if topic_exists(broker, topic):
        clean_topics(broker, [topic])
        while topic_exists(broker, topic):
            time.sleep(1)
    isError = True
    while isError:
        try:
            create_topics(broker, [topic])
            isError = False
        except errors.TopicAlreadyExistsError:
            print("Topic already exists, retrying...")
            clean_topics(broker, [topic])
            time.sleep(1)
    while not topic_exists(broker, topic):
        time.sleep(1)

def get_flink_jobid(log_path="../logs/runner.log"):
    with open(log_path, "r") as f:
        content = f.read()
    match = re.search(r"JobID\s+([a-fA-F0-9]+)", content)
    if match:
        return match.group(1)
    return None

def generate_commands(nr=-1):
    cmds = []
    for data_file, algos in commands.items():
        for algo, modes in algos.items():
            for mode in modes:
                cmds.append((algo, str(mode), data_file, str(data_len[data_file][mode])))
    return cmds if nr == -1 else cmds[nr]

def generate_commands2(nr=-1):
    cmds = []
    for data_file, modes in commands2.items():
        for mode, algos in modes.items():
            for algo in algos:
                cmds.append((algo, str(mode), data_file, str(data_len[data_file][mode])))
    return cmds if nr == -1 else cmds[nr]

def get_message_count(broker='localhost:19092', topic='metrics'):
    consumer = KafkaConsumer(bootstrap_servers=broker)
    partitions = consumer.partitions_for_topic(topic)
    if not partitions:
        return 0

    total = 0
    for p in partitions:
        tp = TopicPartition(topic, p)
        consumer.assign([tp])
        consumer.seek_to_beginning(tp)
        start = consumer.position(tp)
        consumer.seek_to_end(tp)
        end = consumer.position(tp)
        total += end - start
    consumer.close()
    return total

def run_algorithm(num, data_loading_change=True):

    cmd = generate_commands2(num)
    print(f"Running {num} command: {cmd} with data_loading_change={data_loading_change}")
    background_cmd = ["python3", "trackMemInDocker.py", cmd[0], cmd[1], cmd[2]]
    foreground_cmd_load_data = ["java", "-jar", "../jars/data-loader.jar", cmd[1], cmd[2]]
    flink_cmd = ["bash", "run_job.sh", cmd[0], cmd[1], cmd[3]]
    stop_flink_job = ["bash", "stop_job.sh"]
    foreground_scanning_topic = ["java", "-jar", "../jars/data-scanner.jar"]

    # Start the background process
    print("Starting background command...")
    bg_process = subprocess.Popen(background_cmd)

    try:
        # Run the foreground command and wait for it to finish
        print("Running foreground command...")
        print("Cleaning files...")
        clean_files()
        print("Files cleaned.")
        print("Managing Kafka topics...")
        for topic in TOPICS:
            print(f"Managing topic: {topic}")
            if topic == 'input' and not data_loading_change:
                continue
            manage_topic(BROKER, topic)
        print("Kafka topics managed.")

        print("Loading data into Kafka...")

        if data_loading_change:
            with open("../logs/runner.log", "w") as log_file:
                load_process = subprocess.run(foreground_cmd_load_data, stdout=log_file, stderr=subprocess.STDOUT, check=True)
        print("Data loaded into Kafka.")
        print("Starting Flink job...")
        with open("../logs/runner.log", "a") as log_file:
            flink_process = subprocess.Popen(flink_cmd, stdout=log_file, stderr=subprocess.STDOUT)
        amt_of_entries = 0
        timeStart = time.time()
        while amt_of_entries < int(cmd[3]):
            time.sleep(10)
            amt_of_entries = get_message_count()
            time_elapsed = int(time.time() - timeStart)
            print(f"Current amount of entries in Kafka topic 'metrics': {amt_of_entries} and time elapsed: {time_elapsed}s")
            if time_elapsed > 60*30:
                print("Time limit exceeded while waiting for messages in 'metrics' topic.")
                break

        job_id = get_flink_jobid()
        print(f"JobId: {job_id}")
        stop_flink_job.append(job_id)

        print("Stopping Flink job...")
        try:
            subprocess.run(stop_flink_job, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error stopping Flink job: {e}")
        flink_process.terminate()
        flink_process.wait()
        print("Flink job completed.")

        print("Starting foreground scanning topic command...")
        with open("../logs/runner.log", "a") as log_file:
            subprocess.run(foreground_scanning_topic, check=True, stderr=log_file, stdout=log_file)

        print("Foreground scanning topic command completed.")
        print("Plotting metrics...")
        plot_metrics(cmd[0].split("-1.3.0")[0], cmd[1], cmd[2].split(".")[0])
        # print("Running end foreground command...")
        # subprocess.run(foreground_cmd2, check=True)
    finally:
        # Terminate the background process
        print("Terminating background command...")
        bg_process.send_signal(signal.SIGINT)
        # bg_process.terminate()
        bg_process.wait()
        print("Background command terminated.")

    print("Foreground command completed.")

#def run_all():
#     total_cmds = len(generate_commands())
#     for i in range(total_cmds):
#         print(f"Running command {i+1}/{total_cmds}")
#         run_algorithm(i)

def run_all_optimze_loading_data():
    data_loading_change = False
    cnt = 0
    for data_file, modes in commands2.items():
        data_loading_change = True
        for mode, algos in modes.items():
            data_loading_change = True
            for algo in algos:
                run_algorithm(cnt, data_loading_change)
                data_loading_change = False
                cnt += 1

def plot_all():
    for data_file, modes in commands2.items():
        for mode, algos in modes.items():
            for algo in algos:
                plot_metrics(algo.split("-1.3.0")[0], str(mode), data_file.split(".")[0])

if __name__ == "__main__":
    # print(cmd)
    # run_algorithm(17)
    # run_all_optimze_loading_data()
    run_algorithm(17, True)
    # plot_all()