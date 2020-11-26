def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        _p = (a + b + c) / 2
        square = (_p * ((_p - a) * (_p - b) * (_p - c))) ** 0.5
        if square >= 0:
            return True
        else:
            return False
    else:
        return False


is_triangle(1, 2, 2)
is_triangle(-1, 2, 3)
is_triangle(0, 2, 3)
is_triangle(5, 1, 5)