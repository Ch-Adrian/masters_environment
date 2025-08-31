import subprocess
import time
import signal

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

data_len = {
    "web-NotreDame.txt": 1497134,
    "Email-EuAll.txt": 420045,
    "facebook_combined.txt": 88234
}

time_limits = {
    "web-NotreDame.txt": 480,
    "Email-EuAll.txt": 240,
    "facebook_combined.txt": 240
}

def generate_commands(nr=-1):
    cmds = []
    for data_file, algos in commands.items():
        for algo, modes in algos.items():
            for mode in modes:
                cmds.append((algo, str(mode), data_file, str(data_len[data_file]), str(time_limits[data_file])))
    return cmds if nr == -1 else cmds[nr]

cmd = generate_commands(15)
background_cmd = ["python3", "trackMemInDocker.py", cmd[0], cmd[1], cmd[2]]
foreground_cmd = ["bash", "test_algorithm.sh", cmd[0], cmd[1], cmd[3], cmd[2], cmd[4]]

def main():
    # Start the background process
    print("Starting background command...")
    bg_process = subprocess.Popen(background_cmd)

    try:
        # Run the foreground command and wait for it to finish
        print("Running foreground command...")
        subprocess.run(foreground_cmd, check=True)
    finally:
        # Terminate the background process
        print("Terminating background command...")
        bg_process.send_signal(signal.SIGINT)
        # bg_process.terminate()
        bg_process.wait()
        print("Background command terminated.")

    print("Foreground command completed.")

if __name__ == "__main__":
    print(cmd)
    main()