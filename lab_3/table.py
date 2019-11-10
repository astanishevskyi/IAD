import csv
from data_preprocessing import tabulation_with_random, linear_empirical_function, squared_empirical_function


def create_linear_table():
    a_1 = 0.8
    a_2 = -4

    alpha_1 = linear_empirical_function(tabulation_with_random(1))
    alpha_10 = linear_empirical_function(tabulation_with_random(10))
    alpha_100 = linear_empirical_function(tabulation_with_random(100))

    mistake_1_a_1 = abs((a_1 - alpha_1[0]) / alpha_1[0]) * 100
    mistake_1_a_2 = abs((a_2 - alpha_1[1]) / alpha_1[1]) * 100

    mistake_10_a_1 = abs((a_1 - alpha_10[0]) / alpha_10[0]) * 100
    mistake_10_a_2 = abs((a_2 - alpha_10[1]) / alpha_10[1]) * 100

    mistake_100_a_1 = abs((a_1 - alpha_100[0]) / alpha_100[0]) * 100
    mistake_100_a_2 = abs((a_2 - alpha_100[1]) / alpha_100[1]) * 100

    with open('linear.csv', mode='w') as linear_function:
        linear_writer = csv.writer(linear_function, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        linear_writer.writerow(['', 'Вихідна функція', 'alpha = 1', '', 'alpha = 10', '', 'alpha = 100', ''])
        linear_writer.writerow(['', 'Значення', 'Значення', 'Похибка %', 'Значення', 'Похибка %', 'Значення', 'Похибка %'])
        linear_writer.writerow(['а_1', a_1, '{0:.4f}'.format(alpha_1[0]), '{0:.2f}'.format(mistake_1_a_1),
                                '{0:.4f}'.format(alpha_10[0]), '{0:.2f}'.format(mistake_10_a_1),
                                '{0:.4f}'.format(alpha_100[0]), '{0:.2f}'.format(mistake_100_a_1)])
        linear_writer.writerow(['а_2', a_2, '{0:.4f}'.format(alpha_1[1]), '{0:.2f}'.format(mistake_1_a_2),
                                '{0:.4f}'.format(alpha_10[1]), '{0:.2f}'.format(mistake_10_a_2),
                                '{0:.4f}'.format(alpha_100[1]), '{0:.2f}'.format(mistake_100_a_2)])


def create_squared_table():
    a_1 = 0.8
    a_2 = -4
    a_3 = 0
    alpha_1 = squared_empirical_function(tabulation_with_random(1))
    alpha_10 = squared_empirical_function(tabulation_with_random(10))
    alpha_100 = squared_empirical_function(tabulation_with_random(100))

    mistake_1_a_1 = abs((a_1 - alpha_1[2]) / alpha_1[2]) * 100
    mistake_1_a_2 = abs((a_2 - alpha_1[1]) / alpha_1[1]) * 100
    mistake_1_a_3 = abs((a_3 - alpha_1[0]) / alpha_1[0]) * 100

    mistake_10_a_1 = abs((a_1 - alpha_10[2]) / alpha_10[2]) * 100
    mistake_10_a_2 = abs((a_2 - alpha_10[1]) / alpha_10[1]) * 100
    mistake_10_a_3 = abs((a_3 - alpha_10[0]) / alpha_10[0]) * 100

    mistake_100_a_1 = abs((a_1 - alpha_100[2]) / alpha_100[2]) * 100
    mistake_100_a_2 = abs((a_2 - alpha_100[1]) / alpha_100[1]) * 100
    mistake_100_a_3 = abs((a_3 - alpha_100[0]) / alpha_100[0]) * 100

    with open('squared.csv', mode='w') as squared_function:
        squared_writer = csv.writer(squared_function, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        squared_writer.writerow(['', 'Вихідна функція', 'alpha = 1', '', 'alpha = 10', '', 'alpha = 100', ''])
        squared_writer.writerow(['', 'Значення', 'Значення', 'Похибка %', 'Значення', 'Похибка %', 'Значення', 'Похибка %'])
        squared_writer.writerow(['а_1', a_1, '{0:.4f}'.format(alpha_1[2]), '{0:.2f}'.format(mistake_1_a_1),
                                 '{0:.4f}'.format(alpha_10[2]), '{0:.2f}'.format(mistake_10_a_1),
                                 '{0:.4f}'.format(alpha_100[2]), '{0:.2f}'.format(mistake_100_a_1)])
        squared_writer.writerow(['а_2', a_2, '{0:.4f}'.format(alpha_1[1]), '{0:.2f}'.format(mistake_1_a_2),
                                 '{0:.4f}'.format(alpha_10[1]), '{0:.2f}'.format(mistake_10_a_2),
                                 '{0:.4f}'.format(alpha_100[1]), '{0:.2f}'.format(mistake_100_a_2)])
        squared_writer.writerow(['а_3', a_3, '{0:.4f}'.format(alpha_1[0]), '{0:.2f}'.format(mistake_1_a_3),
                                 '{0:.4f}'.format(alpha_10[0]), '{0:.2f}'.format(mistake_10_a_3),
                                 '{0:.4f}'.format(alpha_100[0]), '{0:.2f}'.format(mistake_100_a_3)])


create_linear_table()
create_squared_table()
