# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = list(range(1, 12))


def changing_places():
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]


if len(my_list) == 0:
    print('В списке ничего нет')
elif len(my_list) == 1:
    print('В списке всего 1 элемент')
elif (len(my_list) % 2) == 0 & (len(my_list) != 0):
    changing_places()
    print(my_list)
elif (len(my_list) % 2) != 0:
    last = my_list.pop()
    changing_places()
    my_list.append(last)
    print(my_list)
