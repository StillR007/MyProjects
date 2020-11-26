from functools import reduce
print(reduce(lambda x, y: x*y, (number for number in list(range(20, 1001)) if number % 2 == 0)))
