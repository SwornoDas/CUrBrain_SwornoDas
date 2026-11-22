def suffix_sum_in_place(arr):
    running_sum = 0

    for i in range(len(arr) - 1, -1, -1):
        current_value = arr[i]
        arr[i] = running_sum
        running_sum += current_value