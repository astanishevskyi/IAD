from matplotlib import pyplot as plt


def draw_histogram(frequency_data):
    x = list(frequency_data.keys())
    y = list(frequency_data.values())

    plt.bar(x, height=y)
    plt.grid()
    plt.show()


def draw_distribution(empirical_function):
    x = list(empirical_function.keys())
    y = list(empirical_function.values())

    plt.bar(x, y)
    plt.grid()
    plt.show()
