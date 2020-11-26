def asking(**kwargs):
    print(f'{kwargs}')


name = input('Введите имя')
second_name = input('Введите фамилию')
year = input('Введите год рождения')
city = input('Введите город проживания')
email = input('Введите свой email')
phone = input('Введите телефон')
asking(name=name, second_name=second_name, year=year, city=city, email=email, phone=phone)
