num = int(input("Enter any positive number: "))

a = int(input("Enter single digit a: "))
b = int(input("Enter single digit b: "))

count_a = 0
count_b = 0

while num > 0:
    digit = num % 10

    if digit == a:
        count_a += 1

    if digit == b:
        count_b += 1

    num //= 10

if num == 0:
    if a == 0:
        count_a += 1
    if b == 0:
        count_b += 1

difference = abs(count_a - count_b)

print(difference)