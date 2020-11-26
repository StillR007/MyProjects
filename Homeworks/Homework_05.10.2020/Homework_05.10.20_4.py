def exponentiation(x, y):
    return x ** y


number1 = int(input('Введите действительное положительное число'))
number2 = int(input('Введите целое отрицаельное число'))
print(f'{number1} в степени {number2} равен {exponentiation(number1, number2)}')
