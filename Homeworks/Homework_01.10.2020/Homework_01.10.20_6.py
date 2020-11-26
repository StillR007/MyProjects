count_of_items = 0
goods = []
while True:
    item = input('Введите название товара, цену, количество '
            'и единицу измерения через пробел. Чтобы прекратить, '
            'введите 00')
    if item == "00" and count_of_items == 0:
        print('Вы ничего не ввели')
        break
    elif item == '00' and count_of_items > 0:
        print('Список составлен')
        break
    else:
        item = list((item).split())
        count_of_items += 1
        new_item = {
            'Название:': item[0],
            'Цена:': item[1],
            'Количество:': item[2],
            'ед:': item[3]
        }
        last_item = [count_of_items, new_item]
        last_item = tuple(last_item)
        goods.append(last_item)
print(goods)

def building_answer(key):
    count = 0
    list_of_keys = []
    while count < len(goods):
        list_of_keys.append(goods[count - 1][1][key])
        count += 1
    print(list_of_keys)


user_key = str(input('Введите ключ').lower())
if user_key == 'название':
    building_answer('Название:')
if user_key == 'цена':
    building_answer('Цена:')
if user_key == 'количество':
    building_answer('Количество:')
if user_key == 'ед':
    building_answer('ед:')
