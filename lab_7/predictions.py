from copy import deepcopy


def tomorrow_as_today_2(input_data):
    y = deepcopy(input_data)
    output = [y[0], y[1]]
    for i in range(1, len(input_data) - 1, 1):
        output.append(y[i] + (y[i] - y[i-1]))

    return output


def tomorrow_as_today_3(input_data):
    y = deepcopy(input_data)
    for i in range(24):
        y.append(y[i+1] * (y[i+1] / y[i]))

    return y


def simple_mean(input_data):
    y = deepcopy(input_data)
    for i in range(24):
        y.append(sum(y) / len(y))

    return y


def moving_average(input_data, k=2):
    y = deepcopy(input_data)

    for i in range(len(y), 25, 1):
        y.append(sum(y[i-k:i]) / (k + 1))

    return y


def exponential_mean(input_data, a=0):
    y = deepcopy(input_data)

    for i in range(len(y), 25, 1):
        y_value = a * y[i] + (1 - a) * sum(y[:i])
        y.append(y_value)

    return y
