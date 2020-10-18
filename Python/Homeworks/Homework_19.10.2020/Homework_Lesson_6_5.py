class Stationery:
    def draw(self):
        print('Общий метод отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Метод отрисовки: ручка')


class Pencil(Stationery):
    def draw(self):
        print('Метод отрисовки: карандаш')


class Handle(Stationery):
    def draw(self):
        print('Метод отрисовки: маркер')


a = Pen()
a.draw()
b = Pencil()
b.draw()
c = Handle()
c.draw()
d = Stationery()
d.draw()
