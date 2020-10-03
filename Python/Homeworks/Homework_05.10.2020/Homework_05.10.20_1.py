def division(number1, number2):
    return number1 / number2


x = float(input('Введите первое число'))
y = float(input('Введите второе число'))
if y == 0:
    print('На ноль делить нельзя')
else:
    print(division(x, y))
