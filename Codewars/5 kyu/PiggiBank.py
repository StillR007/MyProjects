import this
class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = int(dollars)
        self.cents = int(cents)
        self.deposit_dollars = 0
        self.deposit_cents = 0
        self.cents_to_doll = 0

    def add_money(self, dollars, cents):
        self.deposit_dollars += dollars
        self.deposit_cents += cents
        if self.deposit_cents >= 100:
            self.cents_to_doll = self.deposit_cents // 100
            self.deposit_cents -= (self.cents_to_doll * 100)
            self.deposit_dollars += self.cents_to_doll
            return self.deposit_dollars, self.deposit_cents
        else:
            return self.deposit_dollars, self.deposit_cents


b = PiggyBank(0, 0)
b.add_money(1, 5)
b.add_money(3, 200)
b.add_money(2, 47)

c = PiggyBank(0, 0)
c.add_money(2, 105)
c.add_money(4, 451)