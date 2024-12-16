def two_sum(num_list, target_value):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[j] == target_value - num_list[i]:
                return [i, j]

num_list = [2, 7, 11, 15]
target_value = 9

result = two_sum(num_list, target_value)
print(result)    # [0, 1]