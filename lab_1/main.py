def my_func(input_data: list) -> list:
    arithmetic_mean = sum(input_data)/len(input_data)
    return [i for i in input_data if i > arithmetic_mean]


data = [i for i in range(1, 11)]
# data = [2, 10, 9, 7, 66, 5, 4, 3, 8, 4]
print(my_func(data))
