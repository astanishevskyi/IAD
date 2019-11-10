from data_preprocessing import *
from graph import draw_histogram, draw_distribution
from input_data import create_input


def main():
    input_data = create_input()
    interval = get_intervals(input_data)
    frequency_data = frequency_histogram(input_data, interval)
    distribution_data = empirical_function_of_distribution(input_data, interval)

    print(input_data)

    draw_histogram(frequency_data)
    draw_distribution(distribution_data)


if __name__ == '__main__':
    main()
