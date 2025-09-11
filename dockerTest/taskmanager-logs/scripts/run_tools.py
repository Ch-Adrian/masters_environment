import subprocess
import signal
import json

taskmanager_log_dir = "../taskmanager-logs/"

tools = json.load(open(taskmanager_log_dir+"scripts/tools.json", "r"))

def run_tool(tool_name):
    tool_cmd = tools[tool_name]
    background_cmd = [tool_cmd]

def setup_toolset(tool_name, data_loading_change=True):
    background_cmd = ["python3", "trackMemInDocker.py", cmd[0], cmd[1], cmd[2]]
    bg_process = subprocess.Popen(background_cmd)

    try:
        print(taskmanager_log_dir+"logs/"+tool_name+".log")
        with open(taskmanager_log_dir+"logs/"+tool_name+".log", "w") as log_file:
            tool_process = subprocess.Popen(flink_cmd, stdout=log_file, stderr=subprocess.STDOUT)
    finally:
        # Terminate the background process
        print("Terminating background command...")
        bg_process.send_signal(signal.SIGINT)
        # bg_process.terminate()
        bg_process.wait()
        print("Background command terminated.")

    print("Foreground command completed.")

def run_all_tools():
    for tool in tools:
        cmd = tools[tool]
        print(f"Running tool: {tool}")
        # run_tool(0, True)

def show_tools():
    for idx, tool in enumerate(tools['tools']):
        print(str(idx)+": "+tool['cmd'][0])

if __name__ == "__main__":
    show_tools()