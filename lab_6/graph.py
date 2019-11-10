import matplotlib.pyplot as plt


def draw_clusters(data, centers, clusters):
    colors = ['orange', 'blue', 'green', 'red']
    for i in range(len(data)):
        plt.scatter(data[i, 0], data[i, 1], s=7, color=colors[clusters[i]])

    plt.scatter(centers[:, 0], centers[:, 1], marker='*', c='black', s=150)
    plt.show()
