my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 58]
new_list = []

for number in range(len(my_list)):
    if number == 0:
        pass
    elif my_list[number - 1] < my_list[number]:
        new_list.append(my_list[number])
    elif number == 0:
        continue
    else:
        continue
print(new_list)
