def EvendigitsCount():
    number = int(input("Enter the number: "))
    
    if number == 0:
        return False

    number = abs(number)
    count = 0

    while number != 0:
        number //= 10
        count += 1

    return count % 2 == 0


print(EvendigitsCount())