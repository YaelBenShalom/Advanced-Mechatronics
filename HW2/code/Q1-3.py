import csv
import argparse
import matplotlib.pyplot as plt  # for plotting
import numpy as np  # for sine function


def main(args):
    if args["csv"]:
        csv_file = args["csv"]
    else:
        csv_file = "data/sigA.csv"

    t = []  # column 0
    data = []  # column 1

    with open(csv_file) as f:
        # open the csv file
        reader = csv.reader(f)
        for row in reader:
            # read the rows 1 one by one
            t.append(float(row[0]))  # leftmost column
            data.append(float(row[1]))  # second column

    # for i in range(len(t)):
    #     # print the data to verify it was read
    #     print(str(t[i]) + ", " + str(data[i]))

    sample_rate = len(t)/t[-1]
    print("\nQuestion 3:")
    print(f"The sample rate is {sample_rate} Hz")

    plt.plot(t, data, 'b-*')
    plt.xlabel('Time [s]')
    plt.ylabel('Signal')
    plt.title(f'Signal vs Time (for {csv_file})')
    # plt.savefig(f'images/plot')
    plt.show()


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv", help="path to the csv file")
    args = vars(parser.parse_args())
    main(args)
