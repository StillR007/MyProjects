class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.weight = 100
        self.depth = 1
        result = length * width * self.weight * self.depth
        print(f'Потребуется {result}кг полотна')


a = Road(2, 30)
