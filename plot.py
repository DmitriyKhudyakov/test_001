import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def plot_points_3d(data, ax, fig=None, color="g"):
    if fig is None:
        fig = plt.figure()
    ax.grid()
    for cd in data:
        ax.scatter(cd[0], cd[1], cd[2], color=color)


def plot_points_2d(data, fig=None, color="g"):
    if fig is None:
        fig = plt.figure()
    plt.grid()
    for cd in data:
        plt.scatter(cd[0], cd[1], color=color, alpha=0.5)


def plot_polynomial_surf(c, polynomial_func, lim_x1, lim_x2, step, title, labels=["x1", "x2", "z"], fig=None):
    if fig is None:
        fig = plt.figure()
    ax = fig.gca(projection="3d")
    plt.title(title)
    ax.set_zlabel(labels[2])
    ax.set_ylabel(labels[1])
    ax.set_xlabel(labels[0])
    x1 = np.arange(lim_x1[0], lim_x1[1], step)
    x2 = np.arange(lim_x2[0], lim_x2[1], step)
    x1, x2 = np.meshgrid(x1, x2)
    z = np.array(polynomial_func(c, x1, x2))
    ax.plot_wireframe(x1, x2, z, cmap=cm.coolwarm, linewidth=0.2, antialiased=False)


def plot_section_polynomial_x1_y_by_x2_values(c, polynomial_func, lim_x1, n_values, sec_val_list, title,
                                              labels=["x1", "y"], fig=None):
    if fig is None:
        fig = plt.figure()
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    for sec_val in sec_val_list:
        x1 = np.linspace(lim_x1[0], lim_x1[1], n_values)
        y = [polynomial_func(c, x1_curr, sec_val) for x1_curr in x1]
        plt.plot(x1, y, label=str(sec_val)+"$^{\circ}$")
    plt.legend()
