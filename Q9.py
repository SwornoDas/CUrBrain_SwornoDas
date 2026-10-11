n = int(input("Enter number: "))

num = n + 1

while True:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime and num > 1:
        print(num)
        break

    num += 1