num = int(input("Enter number: "))

result = []

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        digit = 0

    result.insert(0, digit)
    num //= 10

print(result)