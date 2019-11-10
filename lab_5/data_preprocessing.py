import math


def get_intervals(input_data):
    x_min = min(input_data)
    x_max = max(input_data)

    interval = (x_max - x_min) / (1 + 3.334 * math.log10(len(input_data)))

    return interval


def frequency_histogram(input_data, interval):
    frequency_data = {}
    min_x = min(input_data)

    m = 1 + 3.334 * math.log10(len(input_data))

    for _ in range(int(m)):
        frequency_data[min_x] = 0
        for x in input_data:
            if min_x < x < min_x + interval:
                frequency_data[min_x] = frequency_data[min_x] + 1

        min_x = min_x + interval
    return frequency_data


def empirical_function_of_distribution(input_data, interval):
    empirical_data = {}
    min_x = min(input_data)

    m = 1 + 3.334 * math.log10(len(input_data))

    empirical_data[min_x] = 0

    for _ in range(int(m)):

        for x in input_data:
            if min_x < x < min_x + interval:
                empirical_data[min_x] = empirical_data[min_x] + 1

        previous_value = empirical_data[min_x]
        min_x = min_x + interval
        empirical_data[min_x] = previous_value

    return empirical_data
