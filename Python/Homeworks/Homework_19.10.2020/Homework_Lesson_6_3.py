with_bonus = {
    20000: 5000,
    30000: 10000,
    40000: 20000
}


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self. position = position
        self._income = income + with_bonus[income]


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'доход с премией {self._income}')


Ivan = Position("Ivan", "Smirnov", "Master", 40000)
Ivan.get_full_name()
Ivan.get_total_income()
