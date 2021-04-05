import csv
import argparse
import matplotlib.pyplot as plt # for plotting
import numpy as np # for sine function


def main(args):
    if args["csv"]:
        csv_file = args["csv"]
    else:
        csv_file = "data/sigA.csv"
    
    if csv_file == "data/sigA.csv":
        sampling_rate = "10000Hz"
        f_L = "300Hz"
        b_L = "100Hz"

        # Configuration.
        fS = 10000  # Sampling rate.
        fL = 300  # Cutoff frequency.
        N = 311  # Filter length, must be odd.

    if csv_file == "data/sigB.csv":
        sampling_rate = "3300Hz"
        f_L = "80Hz"
        b_L = "33Hz"

        # Configuration.
        fS = 3300  # Sampling rate.
        fL = 80  # Cutoff frequency.
        N = 311  # Filter length, must be odd.

    if csv_file == "data/sigC.csv":
        sampling_rate = "2500Hz"
        f_L = "100Hz"
        b_L = "25Hz"

        # Configuration.
        fS = 2500  # Sampling rate.
        fL = 100  # Cutoff frequency.
        N = 311  # Filter length, must be odd.

    if csv_file == "data/sigD.csv":
        sampling_rate = "400Hz"
        f_L = "28Hz"
        b_L = "36Hz"

        # Configuration.
        fS = 400  # Sampling rate.
        fL = 28  # Cutoff frequency.
        N = 35  # Filter length, must be odd.

    # Compute sinc filter.
    h = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2))

    # Apply window.
    h *= np.hamming(N)

    # Normalize to get unity gain.
    h /= np.sum(h)




    t = [] # column 0
    data = [] # column 1
    
    with open(csv_file) as f:
        # open the csv file
        reader = csv.reader(f)
        for row in reader:
            # read the rows 1 one by one
            t.append(float(row[0])) # leftmost column
            data.append(float(row[1])) # second column

    ndata = []
    len_diff = len(data) - len(h)

    for i in range(len_diff):
        buffer = []
        for j in range(len(h)):
            buffer.append(data[i + j])
        ndata.append(np.average(buffer, weights=h))

    sample_rate = len(t)/t[-1]
    print(f"The sample rate is {sample_rate} Hz")

    dt = len(t)/t[-1]
    t = np.asarray(t)
    nt = t[0 : len_diff]
    # s = 4.0 * np.sin(2 * np.pi * 100 * t) + 0.25 * np.sin(2 * np.pi * 1000 * t) + 25

    Fs = dt # sample rate
    Ts = 1.0/Fs; # sampling interval
    ts = np.arange(0,t[-1],Ts) # time vector
    y = data # the data to make the fft from
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    nts = np.arange(0,nt[-1],Ts) # time vector
    ny = ndata # the data to make the fft from
    nn = len(ny) # length of the signal
    nk = np.arange(nn)
    nT = nn/Fs
    nfrq = k/nT # two sides frequency range
    nfrq = nfrq[range(int(nn/2))] # one side frequency range
    nY = np.fft.fft(ny)/nn # fft computing and normalization
    nY = nY[range(int(nn/2))]

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title(f'sample_rate = {fS}, f_L = {f_L}, b_L = {b_L}')
    ax1.plot(t,data,'b')
    ax1.plot(nt, ndata, 'r')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Signal')
    ax2.loglog(frq,abs(Y),'b') # plotting the fft
    ax2.loglog(nfrq,abs(nY),'r') # plotting the filtered fft
    ax2.set_xlabel('Freq (Hz)')
    ax2.set_ylabel('|Y(freq)|')
    fig.suptitle(f'Signal vs Time (for {csv_file})')    
    
    plt.show()


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv", help="path to the csv file")
    args = vars(parser.parse_args())
    main(args)