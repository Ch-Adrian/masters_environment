import matplotlib.pyplot as plt

def read_integers(filename):
    """Read integers from a file (one per line)."""
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]

def plot_measurements(file1, file2, data_len):
    data1 = read_integers(file1)
    data2 = read_integers(file2)

    # Ensure both lists have the same length
    min_len = min(len(data1), min(data_len, len(data2)))
    print(min_len)
    data1, data2 = data1[:min_len], data2[:min_len]

    x = [i for i in range(min_len) ]
    plt.plot(x, data1, label="Measurement 1")
    # plt.plot(x, data2, marker="s", label="Measurement 2")

    plt.xlabel("Sample index")
    plt.ylabel("Value")
    plt.title("Comparison of Two Measurements")
    plt.legend()
    plt.grid(True)
    plt.show()

    # fig.savefig("../plots/results/metrics_"+task_name+"_"+mode+"_"+data_file+".png")
    # plt.close()

# Example usage:
# plot_measurements("file1.txt", "file2.txt")


if __name__ == "__main__":

    plot_measurements("../logs/results/metrics_dynamic-connectivity-ett-1_0.log", "../logs/results/metrics_dynamic-connectivity-lct-1_0.log", 42)