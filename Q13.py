def divisible_prefix(arr, k):
    total = 0
    k = abs(k)

    for num in arr:
        total += num

        if total % k == 0:
            return True

    return False


print(divisible_prefix([4, 2, 9], 3))
print(divisible_prefix([1, 2, 4], 5))
print(divisible_prefix([5], 5))
print(divisible_prefix([0, 1], 7))
print(divisible_prefix([-2, 2, 1], 3))