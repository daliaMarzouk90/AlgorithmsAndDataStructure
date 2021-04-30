list_1 = [0 for i in range(5)]
list_2 = [0 for i in range(5)]

list_1 = list_1 + list_2

del list_2

list_2 = [0] * 10

print(list_2)