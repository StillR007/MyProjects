from itertools import count
start = 3
max_number = 100

for number in count(start):
    if number == start:
        print('first number is', number)
    elif number < max_number:
        print('next number is', number)
    else:
        print(f'last number is {number}, I can`t more then {max_number}')
        break
