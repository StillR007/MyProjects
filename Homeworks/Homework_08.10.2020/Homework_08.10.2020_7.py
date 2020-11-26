from functools import reduce
n = int(input('Введите число, чтобы вывести его факториал'))


def fact(n):
    global answer
    answer = int(reduce(lambda x, y: x * y, list(range(1, n + 1))))
    yield answer


for el in fact(n):
    print('answer is', answer)
