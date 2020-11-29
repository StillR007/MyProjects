# Next happy year is the year with only distinct digits, (e.g) 2018
def next_happy_year(year):
    year += 1 # because of Next year
    while True:
        _year = set(list(str(year)))
        if len(_year) != 4:
            year += 1
            continue
        else:
            print(year)
            return year

next_happy_year(1001)
next_happy_year(1123)
next_happy_year(2001)
next_happy_year(2334)
next_happy_year(3331)
next_happy_year(1987)
next_happy_year(5555)
next_happy_year(7712)
next_happy_year(8088)
next_happy_year(8999)