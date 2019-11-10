from matplotlib import pyplot as plt
from data_preprocessing import tabulation, tabulation_with_random, linear_empirical_function, \
    squared_empirical_function, linear_empirical_tabulation, squared_empirical_tabulation


def show_graph():
    alpha = 100
    x = [i[0] for i in tabulation()]
    y = [i[1] for i in tabulation()]

    x_random = [i[0] for i in tabulation_with_random(alpha)]
    y_random = [i[1] for i in tabulation_with_random(alpha)]

    linear_empirical_coefficient = linear_empirical_function(tabulation_with_random(alpha))
    linear_empirical_data = linear_empirical_tabulation(linear_empirical_coefficient)
    x_linear = [i[0] for i in linear_empirical_data]
    y_linear = [i[1] for i in linear_empirical_data]

    squared_empirical_coefficient = squared_empirical_function(tabulation_with_random(alpha))
    squared_empirical_data = squared_empirical_tabulation(squared_empirical_coefficient)
    x_squared = [i[0] for i in squared_empirical_data]
    y_squared = [i[1] for i in squared_empirical_data]

    plt.title('y = 0.8 - 4 * x')
    line_1 = plt.plot(x, y, label='Input function')
    line_2 = plt.plot(x_random, y_random, label='Function with random')
    line_3 = plt.plot(x_linear, y_linear, label='Linear empirical function')
    line_4 = plt.plot(x_squared, y_squared, label='Squared empirical function')
    plt.legend()
    plt.show()


show_graph()
