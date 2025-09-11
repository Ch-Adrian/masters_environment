import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys
import numpy as np

def plot_metrics(task_name, task, data_file):
    with open("../logs/metrics.log", "r") as file:
    # with open("../logs/results/metrics_"+task_name+"_"+mode+"_"+data_file+".log", "r") as file:
        content = file.readlines()
        with open("../logs/results/metrics_"+task_name+"_"+task+"_"+data_file+".log", "w") as new_file:
            new_file.writelines(content)

        # task_nr, timestamp, rate
        content = [(int(line.split(",")[3]), int(line.split(",")[0]), line.split(",")[2]) for line in content]
        data = dict()
        lowest_timestamp = min([line[1] for line in content])
        highest_timestamp = max([line[1] for line in content])
        # print("Lowest timestamp: ", lowest_timestamp)
        # print("Highest timestamp: ", highest_timestamp)
        difference = highest_timestamp - lowest_timestamp
        amt_bins = difference//1000000000 + 1
        # print("Difference: ", difference)
        rate_bins = dict()
        for line in content:
            bin_index = (line[1] - lowest_timestamp)//1000000000
            task_nr = int(line[0])
            if task_nr not in rate_bins:
                rate_bins[task_nr] = [[] for _ in range(amt_bins)]
            rate_bins[task_nr][bin_index].append(float(line[2]))


        x = np.array([i for i in range(amt_bins)])
        amt_of_tasks = len(rate_bins.items())
        # print("rate bins: ", len(rate_bins.items()))
        # for key in rate_bins:
        #     print("Task ", key, " has ", len(rate_bins[key]), " bins.")
        #     for i in range(len(rate_bins[key])):
        #         print("Bin ", i, " has ", len(rate_bins[key][i]), " entries.")

        summed = []
        for key in range(len(rate_bins.items())):
            y = []
            for i in range(len(rate_bins[key])):
                if len(rate_bins[key][i]) == 0:
                    y.append(0)
                else:
                    y.append(sum(rate_bins[key][i])/len(rate_bins[key][i]))
            # print(len(y))
            assert len(y) == amt_bins
            summed.append(y)
            if amt_of_tasks == 1:
                plt.plot(x, y, label="Rate (edges/s)", linewidth=1)
            else:
                plt.plot(x, y, label="Node's: "+str(key)+" rate (edges/s)", linewidth=1)

        assert len(rate_bins.items()) == 4
        if len(rate_bins.items()) != 1:
            summed = np.array(summed).sum(axis=0)
            assert len(summed) == amt_bins
            plt.plot(x, summed, label="Overall rate (edges/s)", linewidth=2)

        plt.ylabel('Seconds')
        plt.xlabel('Number of processed edges')
        plt.title('Processing rate over time for '+data_file)
        plt.legend()
        # content = np.array([data[i] for i in sorted(data.keys())])
        # content = content.sum(axis=1)
        # print(len(content))
        # content = np.array([ float(i) for i in content])
        # print(content[:30])

        # plt.plot(content)
        # x = np.array([i for i in range(amt_bins)])
        # fig, ax = plt.subplots()
        # ax.plot(x, content)
        # ax.yaxis.set_major_locator(MaxNLocator(nbins=15))
        # ax.set_ylabel('Seconds')
        # ax.set_xlabel('Number of processed edges')
        # ax.set_title('Processing rate over time for '+data_file)

        plt.savefig("../plots/results/metrics_"+task_name+"_"+task+"_"+data_file+".svg")
        plt.close()

if __name__ == "__main__":
    plot_metrics(sys.argv[1].split("-1.3.0")[0], sys.argv[2], sys.argv[3].split(".")[0])