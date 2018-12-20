import numpy as np
from pandas import DataFrame as df
import matplotlib.pyplot as plt

x_max = 1000.0
x_min = -1000.0

a = 85.0
b = 170.0


def red(x):
    if x > 0:
        return -a / x_max * x + 255.0
    else:
        return -b / x_min * x + 255.0


def green(x):
    if x > 0:
        return -b / x_max * x + 255.0
    else:
        return -b / x_min * x + 255.0


def blue(x):
    if x > 0:
        return -b / x_max * x + 255.0
    else:
        return -a / x_min * x + 255.0


def rgb(x):
    return [red(x) / 255.0, green(x) / 255.0, blue(x) / 255.0]


def main():
    data = [rgb(x) for x in range(int(x_min), int(x_max))]
    x = np.arange(0, x_max - x_min)
    height = np.ones(int(x_max - x_min))
    plt.bar(x, height, color=data, width=1.1)
    plt.show()


if __name__ == "__main__":
    main()
