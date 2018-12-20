import numpy as np
from pandas import DataFrame as df
import matplotlib.pyplot as plt

x_max = 100.0
x_min = -100.0


def red(x):
    if x > 0:
        return -np.power(40, x / x_max) + 256
    else:
        return -np.power(190, -x / x_min) + 256


def green(x):
    if x > 0:
        return -np.power(190, x / x_max) + 256
    else:
        return -np.power(190, -x / x_min) + 256


def blue(x):
    if x > 0:
        return -np.power(190, x / x_max) + 256
    else:
        return -np.power(40, -x / x_min) + 256


def rgb(x):
    return [red(x) / 256, green(x) / 256, blue(x) / 256]


def main():
    data = [rgb(x) for x in range(int(x_min), int(x_max))]
    x = np.arange(0, x_max - x_min)
    height = np.ones(int(x_max - x_min))
    plt.bar(x, height, color=data, width=1.1)
    plt.show()


if __name__ == "__main__":
    main()
