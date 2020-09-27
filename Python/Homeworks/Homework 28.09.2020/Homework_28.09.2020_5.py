profit = int(input("Введите свою выручку:"))
expenditure = int(input("Введите свои расходы:"))
if profit > expenditure:
    print('Ваша выручка больше расходов')
    print("Соотношение выручки к расходам составляет ", profit / expenditure)
    count_of_employyes = int(input("Введите количество работников"))
    print("Прибыль на сотрудника составляет:", (profit - expenditure) / count_of_employyes)
elif profit == expenditure:
    print("Ваша выручка равна расходам")
else:
    print("Ваши расходы больше доходов")
