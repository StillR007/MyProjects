def maskify(string):
    if len(string) >= 4:
        _secret_text = string[:(len(string)-4)]
        _needed_text = string[len(string)-4:]
        for letter in _secret_text:
            _secret_text = _secret_text.replace(letter, "#")
        return _secret_text + _needed_text
    else:
        return string


maskify("Skippy")
maskify("Nananananananananananananananana Batman!")
maskify("1%5")
