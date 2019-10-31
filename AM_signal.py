import numpy as np
import matplotlib.pyplot as plt


def DSBLC_singal(amp=5, modulation_index=1, freq_of_carrier_signal=1200, freq_of_message_signal=300):
    X = np.linspace(-5, 5, 1000)
    formula = 2 * np.cos(1500 * np.pi * X) + 2 * \
        np.cos(900 * np.pi * X) + 7 * np.cos(1200 * np.pi * X)

    plt.plot(X, formula, color="red", alpha=0.5)

    plt.show()


if __name__ == '__main__':
    DSBLC_singal()
