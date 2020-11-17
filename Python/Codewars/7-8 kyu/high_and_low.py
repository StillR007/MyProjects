def high_and_low(numbers):
    new_numbers = numbers.split()
    maximum = max(new_numbers)
    minimal = min(new_numbers)
    numbers = str(f'{maximum} {minimal}')
    return numbers


high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
high_and_low("4 5 29 54 4 0 -214 842 -64 1 -3 568 -6") # return "842 -214"