import numpy as np
import matplotlib.pyplot as plt

def DSBLC_singal(amp=5, modulation_index=1, freq_of_carrier_signal=1200, freq_of_message_signal=300,size = 1000):

    X = np.linspace(-5, 5, size)
    formula = 2 * np.cos((freq_of_message_signal+freq_of_carrier_signal) * np.pi * X) + 2 * \
        np.cos((freq_of_carrier_signal-freq_of_message_signal) * np.pi * X) + 7 * np.cos(freq_of_carrier_signal * np.pi * X)

    # if add AWGN
    mu , sigma = 0, 0.1
    s = np.random.normal(mu, sigma,size)
    formula += s

    plt.plot(X, formula, color="red", alpha=0.5)

    plt.show()


if __name__ == '__main__':
    DSBLC_singal()
