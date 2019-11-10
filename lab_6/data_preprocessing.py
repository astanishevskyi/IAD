from copy import deepcopy
import numpy as np


def k_means_algorithm(data):
    # Number of clusters
    clusters_number = 4
    # Number of training data
    points_number = data.shape[0]
    # Number of features in the data
    c = data.shape[1]

    # Generate random centers, here we use sigma and mean to ensure it represent the whole data
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    centers = np.random.randn(clusters_number, c) * std + mean

    centers_old = np.zeros(centers.shape)
    centers_new = deepcopy(centers)

    clusters = np.zeros(points_number)
    distances = np.zeros((points_number, clusters_number))
    error = np.linalg.norm(centers_new - centers_old)

    while error != 0:
        # Measure the distance to every center
        for i in range(clusters_number):
            distances[:, i] = np.linalg.norm(data - centers[i], axis=1)

        # Assign all training data to closest center
        clusters = np.argmin(distances, axis=1)

        centers_old = deepcopy(centers_new)
        # Calculate mean for every cluster and update the center
        for i in range(clusters_number):
            centers_new[i] = np.mean(data[clusters == i], axis=0)

        error = np.linalg.norm(centers_new - centers_old)

    return clusters, centers_new
