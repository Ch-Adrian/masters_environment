import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys

def main(task_name, mode, data_file):
    with open("../logs/metrics.log", "r") as file:
        content = file.readlines()
        with open("../logs/results/metrics_"+task_name+"_"+mode+"_"+data_file+".log", "w") as new_file:
            new_file.writelines(content)
        content = [ int(i) for i in content]
        # print(content[:30])

        # plt.plot(content)
        fig, ax = plt.subplots()
        ax.plot([i for i in range(len(content))], content)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=15))


        fig.savefig("../plots/results/metrics_"+task_name+"_"+mode+"_"+data_file+".png")
        plt.close()

if __name__ == "__main__":
    main(sys.argv[1].split("-1.3.0")[0], sys.argv[2], sys.argv[3].split(".")[0])