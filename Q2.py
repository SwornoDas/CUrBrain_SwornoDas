def reverse_and_double(n: int) -> int:
    if n == 0:
        return 0

    mul = -1 if n < 0 else 1
    n = abs(n)

    rev = 0

    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    rev = rev * mul

    return rev * 2


num = int(input("Enter num: "))
print(reverse_and_double(num))




