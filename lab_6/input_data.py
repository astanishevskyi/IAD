import numpy as np


center_1 = [0, -1]
center_2 = [2, 2]
center_3 = [-4, -3]
center_4 = [1, 1]

# Generate random data and center it to the three centers
data_1 = np.random.randn(50, 2) + center_1
data_2 = np.random.randn(50, 2) + center_2
data_3 = np.random.randn(50, 2) + center_3
data_4 = np.random.randn(50, 2) + center_4

data = np.concatenate((data_1, data_2, data_3, data_4), axis=0)

# plt.scatter(data[:, 0], data[:, 1])
#
# plt.show()
