numbers = 'something'
all_results = []
end = None


def going_to_int():
    global i
    i = 0
    while i < len(numbers):
        if numbers[i] == '@':
            numbers.remove('@')
            global end
            end = 0
        else:
            numbers[i] = int(numbers[i])

        i += 1


def sum_of_numbers():
    result = sum(numbers)
    print(f'сумма введенных чисел равна {result}')
    # добавляем в список с результатами
    all_results.append(result)


numbers = 'something'
while numbers:
    numbers = input('Введите числа через пробел. Чтобы прекратить, введите @').split()
    going_to_int()
    sum_of_numbers()
    if end == 0:
        break
print(f'общая сумма: {sum(all_results)}')
