import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plot as cpl
import approximation as apr


N = 10


def polynomial(c, x1, x2):
    res = 0.0
    res += c[0]
    res += c[1] * x1 + c[2] * x2
    res += c[3] * x1 ** 2 + c[4] * x1 * x2 + c[5] * x2 ** 2
    res += c[6] * x1 ** 3 + c[7] * x1 ** 2 * x2 + c[8] * x1 * x2 ** 2 + c[9] * x2 ** 3
    return res


def error(data, c):
    err = 0.0
    for i in range(len(data)):
        err += abs((data[i][2] - polynomial(c, data[i][0], data[i][1])) / data[i][2])
    return err / float(len(data))


def plot_data(c, data, title):
    # first figure
    labels = ["T кипения", "T конденсации", "Q холодопроизводительность"]
    fig = plt.figure()
    ax = Axes3D(fig)
    cpl.plot_points_3d(data, ax, fig, color="r")
    cpl.plot_polynomial_surf(c, polynomial, [-60.0, 30.0], [10.0, 70.0], 1.0, title, labels, fig)
    plt.show()
    # second figure
    labels = ["T кипения", "Q холодопроизводительность"]
    fig = plt.figure()
    data_x1_y = [[cd[0], cd[2]] for cd in data]
    cpl.plot_points_2d(data_x1_y, fig, color="r")
    cpl.plot_section_polynomial_x1_y_by_x2_values(c, polynomial, [-45.0, 10.0], 25, [30.0, 40.0, 50.0],
                                                  title, labels, fig)
    plt.show()


def print_data(c, data, title):
    print("Значения коэффициентов полинома для " + title + ": ")
    i = 0
    for c_curr in c:
        i += 1
        print("     c" + str(i) + " = ", c_curr)
    print("Средняя ошибка аппроксимации: error = ", error(data, c) * 100.0, " %")


def run(data, titles):
    global N
    for curr_data, curr_title in zip(data, titles):
        c = apr.calc(curr_data, N)
        print_data(c, curr_data, curr_title)
        plot_data(c, curr_data, curr_title)
