import numpy as np
from numpy.ma import arange
from random import uniform


def my_function(x: float):
    return 0.8 - 4 * x


def tabulation():
    return [(i, my_function(i)) for i in arange(-5, 5, 0.1)]


def tabulation_with_random(alpha: int):
    return [(i, my_function(i) + alpha * uniform(0, 0.5)) for i in arange(-5, 5, 0.1)]


def linear_empirical_function(input_data):
    n = len(input_data)
    x = [i[0] for i in input_data]
    y = [i[1] for i in input_data]

    sum_x = sum(x)
    sum_y = sum(y)

    sum_x_y = 0
    for i in range(n):
        sum_x_y += x[i] * y[i]

    sum_x_squared = 0
    for i in range(n):
        sum_x_squared += x[i] ** 2

    denominator = (n * sum_x_squared - (sum_x ** 2))

    a_1 = ((sum_y * sum_x_squared) - (sum_x_y * sum_x)) / denominator
    a_2 = (n * sum_x_y - sum_x * sum_y) / denominator

    return [a_1, a_2]


def linear_empirical_tabulation(input_coefficient):
    a_1 = input_coefficient[0]
    a_2 = input_coefficient[1]
    output = [(i, a_2 * i + a_1) for i in arange(-5, 5, 0.1)]
    return output


def squared_empirical_function(input_data):
    n = len(input_data)
    x = [i[0] for i in input_data]
    y = [i[1] for i in input_data]

    x_to_second_power = [i ** 2 for i in x]
    x_to_third_power = [i ** 3 for i in x]
    x_to_forth_power = [i ** 4 for i in x]

    sum_x = sum(x)
    sum_x_second_power = sum(x_to_second_power)
    sum_x_third_power = sum(x_to_third_power)
    sum_x_forth_power = sum(x_to_forth_power)

    sum_x_squared_y = 0
    for i in range(n):
        sum_x_squared_y += (x[i] ** 2) * y[i]

    sum_x_y = 0
    for i in range(n):
        sum_x_y += x[i] * y[i]

    sum_y = sum(y)

    coefficient = np.array([
        [sum_x_forth_power, sum_x_third_power, sum_x_second_power],
        [sum_x_third_power, sum_x_second_power, sum_x],
        [sum_x_second_power, sum_x, n]
        ])

    value = np.array([sum_x_squared_y, sum_x_y, sum_y])
    a = np.linalg.solve(coefficient, value)

    return a


def squared_empirical_tabulation(input_coefficient):
    a_3 = input_coefficient[0]
    a_2 = input_coefficient[1]
    a_1 = input_coefficient[2]
    output = []
    for i in arange(-5, 5, 0.1):
        y = a_3 * (i ** 2) + a_2 * i + a_1
        output.append([i, y])
        y = 0

    return output
