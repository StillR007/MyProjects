def is_isogram(string):
    string.lower()
    for letter in string:
        _a = string.count(letter)
        if _a > 1:
            return False
        else:
            if letter == string[-1]:
                return True
            else:
                pass

is_isogram("RrrrOmaa")