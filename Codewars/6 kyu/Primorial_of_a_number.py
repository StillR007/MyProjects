"""
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied,
only prime numbers are multiplied to calculate the primorial of a number. It's denoted with
P# and it is the product of the first n prime numbers.
"""
from functools import reduce


def num_primorial(n):
    numbers = []
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, num)):
            if len(numbers) < n:
                numbers.append(num)
    return reduce(lambda x, y: x * y, numbers)



num_primorial(3)  # 30
num_primorial(4)  # 210
num_primorial(5)  # 2310
num_primorial(8)  # 9699690
num_primorial(9)  # 223092870
