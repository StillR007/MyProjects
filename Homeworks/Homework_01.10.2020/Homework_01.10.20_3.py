user_month = int(input('Введите номер месяца в виде целого числа'))
# Решение через список
months = ['зима', 'весна', 'лето', 'осень']
if 0 < user_month <= 2 or user_month == 12:
    print(f'это {months[0]}')
elif 3 <= user_month <= 5:
    print(f'это {months[1]}')
elif 6 <= user_month <= 8:
    print(f'это {months[2]}')
elif 9 <= user_month <= 11:
    print(f'это {months[3]}')

# Решение через словарь
user_month2 = int(input('Введите номер месяца'))
months2 = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
           6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
           11: 'осень', 12: 'зима'}
print(f'судя по словарю, это {months2[user_month2]}')
