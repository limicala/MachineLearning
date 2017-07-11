import numpy as np
import matplotlib.pyplot as plt

def draw_plot():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    z = np.cos(x**2)

    plt.plot(x, y, label="sin(x)", color="red")

    plt.plot(x, z, "b--", label="cos(x^2)")


    plt.xlabel("Time")
    plt.ylabel("Volt")

    plt.legend()
    plt.show()

def draw_scatter():
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.scatter(x, y)

    plt.show()


if __name__ == '__main__':
    draw_scatter()