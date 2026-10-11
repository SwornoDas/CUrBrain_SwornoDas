list1 = []
list2 = []

n1 = int(input("Enter size of first list: "))
for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("Enter size of second list: "))
for i in range(n2):
    list2.append(int(input("Enter element: ")))

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements =", common)