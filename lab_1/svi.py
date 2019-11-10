def min_random(input_data: list):
    lengthOfArray = len(input_data) - 1
    for i in range(lengthOfArray):
        for j in range(lengthOfArray - i):
            if input_data[j] < input_data[j + 1]:
                input_data[j], input_data[j + 1] = input_data[j + 1], input_data[j]

    return input_data

# data = [1, 2, 5, 11, 3, 8, 10, 3, 0]
data = [_ for _ in range(1, 10)]
print(min_random(data))
