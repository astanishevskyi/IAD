import math

from numpy.ma import arange


def my_function(x):
    return math.cos(x) * math.e ** (-abs(x))


def tabulation():
    output = []
    for i in arange(-10, 10, 0.1):
        output.append((i, my_function(i)))

    return output


def group_by_alphabet():
    output = []
    names = ['Andrew', 'Olena', 'Anton', 'Roman', 'Oleh', 'Sviatozar', 'Ramzan', 'Oleksandr']

    for i in names:
        temp = []
        for j in names:
            if i[0] == j[0]:
                 temp.append(j)

        if temp in output:
            continue
        else:
            output.append(temp)

    return output


print(group_by_alphabet())
