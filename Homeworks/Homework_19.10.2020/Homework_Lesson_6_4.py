class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'текущая скорость {self.name} автомобиля {self.speed}')


class TownCar(Car):

    def __init__(self):
        self.is_police = False
        self.name = 'TownCar'
        self.speed = 80

    def show_speed(self):
        print(f'скорость городского автомобиля {self.speed}')
        if self.speed > 60:
            print('Скорость превышена!')


class SportCar(Car):

    def __init__(self):
        self.speed = 120
        self.name = 'SportCar'
        self.color = 'red'
        self.is_police = False


class WorkCar(Car):

    def __init__(self):
        self.name = 'WorkCar'
        self.color = 'grey'
        self.is_police = False
        self.speed = 80

    def show_speed(self):
        print(f'скорость рабочего автомобиля {self.speed}')
        if self.speed > 40:
            print('Скорость превышена!')


class PoliceCar(Car):

    def __init__(self):
        self.name = 'PoliceCar'
        self.is_police = True
        self.color = 'usually police car color'


my_car = SportCar()
my_brother_car = PoliceCar()
my_wife_car = WorkCar()
your_mother_car = TownCar()

print(my_car.speed)
your_mother_car.turn("left")
my_wife_car.show_speed()
