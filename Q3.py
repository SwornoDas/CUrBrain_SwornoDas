num = int(input("Enter num: "))

temp = num
rev = 0

if num < 0:
    sign = -1
    
else:
    sign = 1

num = abs(num)

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

rev *= sign

if temp == rev and temp >= 0:
    print(temp)
    
else:
    print(temp + rev)
