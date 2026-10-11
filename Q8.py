n = int(input("Enter n: "))
k = int(input("Enter k: "))

factors = []

for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)

if k <= len(factors):
    print("Kth factor =", factors[k - 1])
else:
    print(-1)