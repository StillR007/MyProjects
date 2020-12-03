"""
Task is to find out which one of the given numbers differs from the others.
"""


def iq_test(numbers):
    odd_count = 0
    even_count = 0
    numbers = numbers.split(' ')
    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            odd_count += 1
            odd = numbers.index(str(num)) + 1
        else:
            even_count += 1
            even = numbers.index(str(num)) + 1
    if odd_count == 1:
        return odd
    if even_count == 1:
        return even


iq_test("2 4 7 8 10")
iq_test("1 2 2")
