import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys
import numpy as np

def plot_metrics(task_name, mode, data_file):
    with open("../logs/metrics.log", "r") as file:
    # with open("../logs/results/metrics_"+task_name+"_"+mode+"_"+data_file+".log", "r") as file:
        content = file.readlines()
        with open("../logs/results/metrics_"+task_name+"_"+mode+"_"+data_file+".log", "w") as new_file:
            new_file.writelines(content)
        content = np.array([ int(i) for i in content])
        # print(content[:30])

        # plt.plot(content)
        x = np.array([i for i in range(len(content))])
        fig, ax = plt.subplots()
        ax.plot(x, content)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=15))
        ax.set_ylabel('Nanoseconds')
        ax.set_xlabel('Number of processed edges')
        ax.set_title('Metrics over Time for '+data_file)

        fig.savefig("../plots/results/metrics_"+task_name+"_"+mode+"_"+data_file+".svg")
        plt.close()

if __name__ == "__main__":
    plot_metrics(sys.argv[1].split("-1.3.0")[0], sys.argv[2], sys.argv[3].split(".")[0])