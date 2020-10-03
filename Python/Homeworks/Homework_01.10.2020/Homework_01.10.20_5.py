my_list = [7, 5, 3, 3, 2]
while True:
    new_symbol = int(input('Введите новое число. Чтобы прекратить, введите "00"'))
    if new_symbol == 00:
        break
    if new_symbol >= max(my_list):
        my_list.insert(0, new_symbol)
    place = my_list.index(new_symbol)
    print(place)
    if my_list.index(new_symbol) != False:
        my_list.insert(place, new_symbol)
print(my_list)
