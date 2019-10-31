import numpy as np
import matplotlib.pyplot as plt
import random as rand
import os

plt.style.use('bmh')


def discrete_Map(num, height):
    my_array = []
    for x in range(0, num):
        my_array.append(rand.randint(0, height))
    y = np.linspace(1, height, num)
    print(len(my_array), len(y))

    ax = plt.figure()
    ax = plt.subplot(111)
    ax.scatter(y, my_array)
    plt.show()


def ramble_Walk(num=5000, height=1000, saveFile=True, showing=True):
    x_result1 = [height / 2]
    y_result1 = [height / 2]
    x_result2 = [height / 2]
    y_result2 = [height / 2]
    x_result3 = [height / 2]
    y_result3 = [height / 2]
    x_result4 = [height / 2]
    y_result4 = [height / 2]

    for x in range(1, num):

        x_result1.append(rand.randint(-1, 1) + x_result1[-1])
        y_result1.append(rand.randint(-1, 1) + y_result1[-1])

        x_result2.append(rand.randint(-1, 1) + x_result2[-1])
        y_result2.append(rand.randint(-1, 1) + y_result2[-1])

        x_result3.append(rand.randint(-1, 1) + x_result3[-1])
        y_result3.append(rand.randint(-1, 1) + y_result3[-1])

        x_result4.append(rand.randint(-1, 1) + x_result4[-1])
        y_result4.append(rand.randint(-1, 1) + y_result4[-1])

    ax = plt.figure()
    ax = plt.subplot(111)
    point_numbers = list(range(num))

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    ax.scatter(x_result1, y_result1, c=point_numbers,
               cmap=plt.cm.Reds, s=1, label="first")
    ax.scatter(x_result2, y_result2, c=point_numbers,
               cmap=plt.cm.Purples, s=1, label="second")
    ax.scatter(x_result3, y_result3, c=point_numbers,
               cmap=plt.cm.Blues, s=1, label="third")
    ax.scatter(x_result4, y_result4, c=point_numbers,
               cmap=plt.cm.Greens, s=1, label="forth")

    if(showing):
        plt.show()


if __name__ == '__main__':
    ramble_Walk(50000)
