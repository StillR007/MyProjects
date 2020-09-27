#my_list1 = [2, 5, 8, 2, 12, 12, 12, 4, 2]
#my_list2 = [2, 7, 12, 4]
#my_list1 = set(my_list1)
#my_list2 = set(my_list2)
#result = my_list1 - my_list2
#print(result)

a = [1, 1, 1, 2, 2, 2, 3, 4]
b = [2, 4, 5]

for number in a[:]:
    if number in b:
        a.remove(number)

print(a)
