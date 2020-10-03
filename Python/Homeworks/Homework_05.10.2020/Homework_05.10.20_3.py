def my_func(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2


my_list = []
number1 = int(input('Введите первое число'))
number2 = int(input('Введите второе число'))
number3 = int(input('Введите третье число'))
my_list.append(number1)
my_list.append(number2)
my_list.append(number3)
print(f'сумма двух максимальных значений равна: {my_func(my_list)}')
