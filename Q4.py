num = int(input("Enter num: "))

original_num = abs(num)

digit_sum = 0

digit_product = 1

while original_num != 0:
    digit = original_num % 10
    digit_sum += digit
    digit_product *= digit
    original_num //= 10

difference = digit_product - digit_sum

print(f"Difference is: {difference}")