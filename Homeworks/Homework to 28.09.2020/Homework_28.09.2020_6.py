a = float(input('Введите количество километров, которые спортсмен пробежал в первый день'))
b = float(input('Введите желаемое количество километров'))
days_gone = int(0)
while a <= b:
    a += a/10
    days_gone += 1
    print(days_gone, "день:", a, "километров")

print("Понадобилось", days_gone, "дней")