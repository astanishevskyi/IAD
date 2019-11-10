from input_data import data
from data_preprocessing import k_means_algorithm
from graph import draw_clusters


def main():
    clusters, centers = k_means_algorithm(data)
    draw_clusters(data, centers, clusters)


if __name__ == "__main__":
    main()
