from random import randint
numbers = []
count_of_numbers = 8
_i = 1
with open('My_file_5.txt', 'x+') as my_file:
    while _i <= count_of_numbers:
        numbers.append(randint(1, 10))
        my_file.writelines(f'{str(numbers[_i - 1])}\n')
        _i += 1
print(f'Сумма чисел равна {sum(numbers)}\nСоздан файл "My_file_5.txt"')
