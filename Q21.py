def delete_first_occurrence(arr, target):
    index = -1

    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            break

    if index == -1:
        return

    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    del arr[-1]