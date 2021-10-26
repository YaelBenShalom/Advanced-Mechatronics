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

    dt = len(t)/t[-1]
    t = np.asarray(t)
    # s = 4.0 * np.sin(2 * np.pi * 100 * t) + 0.25 * np.sin(2 * np.pi * 1000 * t) + 25

    Fs = dt  # sample rate
    Ts = 1.0/Fs  # sampling interval
    ts = np.arange(0, t[-1], Ts)  # time vector
    y = data  # the data to make the fft from
    n = len(y)  # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T  # two sides frequency range
    frq = frq[range(int(n/2))]  # one side frequency range
    Y = np.fft.fft(y)/n  # fft computing and normalization
    Y = Y[range(int(n/2))]

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title(f'Signal vs Time (for {csv_file})')
    ax1.plot(t, data, 'b')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Signal')
    ax2.loglog(frq, abs(Y), 'b')  # plotting the fft
    ax2.set_xlabel('Freq (Hz)')
    ax2.set_ylabel('|Y(freq)|')

    plt.show()


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv", help="path to the csv file")
    args = vars(parser.parse_args())
    main(args)
