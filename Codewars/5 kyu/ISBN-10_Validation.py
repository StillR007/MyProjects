"""
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9.
The last digit can be 0-9 or X, to indicate a value of 10.
An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.
"""


def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    if isbn.isdigit():
        if sum([int(val) * int(num) for val, num in enumerate(isbn, start=1)]) % 11 == 0:
            return True
        else:
            return False
    elif isbn[:len(isbn) - 1].isdigit() and isbn[len(isbn) - 1] == 'X':
        if (sum([int(val) * int(num) for val, num in enumerate(isbn[0:len(isbn)-1], start=1)]) + 100) % 11 == 0:
            print(sum([int(val) * int(num) for val, num in enumerate(isbn[0:len(isbn)-2], start=1)]) + 100)
            return True
        else:
            return False
    else:
        return False


valid_ISBN10('1112223339')  # True
valid_ISBN10('048665088X')  # True
valid_ISBN10('1293000000')  # True
valid_ISBN10('1234554321')  # True
valid_ISBN10('1234512345')  # False
valid_ISBN10('1293')  # False)
valid_ISBN10('X123456788')  # False
valid_ISBN10('ABCDEFGHIJ')  # False
valid_ISBN10('XXXXXXXXXX')  # False
