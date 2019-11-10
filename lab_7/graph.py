from predictions import tomorrow_as_today_2, tomorrow_as_today_3
import matplotlib.pyplot as plt


def plot_tomorrow_as_today(input_data):
    x = list(input_data.keys())
    y = list(input_data.values())

    # raw_data_for_prediction = y[:2]

    predicted_data_1 = tomorrow_as_today_2(y)
    print(y)
    print(predicted_data_1)
    predicted_data_2 = tomorrow_as_today_3(y)

    plt.plot(x, y)
    plt.plot(x, predicted_data_1)
    # plt.plot(x, predicted_data_2)

    plt.show()
