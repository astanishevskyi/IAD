import matplotlib.pyplot as plt
from data_preprocessing import tabulation


def bar_chart():
    # fig, ax = plt.subplot()
    # fig.set_size_inches(15, 10)
    # ax.set(ylim=[800000, 1300000])

    data = {
        1989: 1228093,
        1990: 1229233,
        1991: 1233676,
        1992: 1235875,
        1993: 1239752,
        1994: 1234991,
        1995: 1224904,
        1996: 1213394,
        1997: 1199592,
        1998: 1185943,
        1999: 1171627,
        2000: 1155993,
        2001: 1139979,
        2002: 1125704,
        2003: 1109306,
        2004: 1093609,
        2005: 1077504,
        2006: 1060763,
        2007: 1046668,
        2008: 1033325,
        2009: 1020612,
        2010: 1011367,
        2011: 1003572,
        2012: 996005,
        2013: 988756,
        2014: 981150,
    }

    labels = list(data.keys())
    value = list(data.values())
    # plt.ylim([950000, 1300000])

    plt.bar(labels, height=value)
    plt.show()


def pie_chart():
    labels = 'Міське населення', 'Сільське населення'
    city = 694538
    village = 461455

    x = [city, village]
    explode = (0, 0.1)

    plt.pie(x, labels=labels, explode=explode, shadow=True, autopct='%1.0f%%')
    plt.show()


def draw_graph():
    x = [i[0] for i in tabulation()]
    y = [i[1] for i in tabulation()]

    line1 = plt.plot(x, y)

    plt.show()


draw_graph()
pie_chart()
bar_chart()
