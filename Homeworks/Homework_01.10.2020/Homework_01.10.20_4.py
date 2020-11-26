user_input = input('Введите строку из нескольких слов с пробелами').split()
i = 0
while i < len(user_input):
    if len(user_input[i]) > 10:
        user_input[i] = user_input[i][:10]
    print(f'{i+1}. {user_input[i]}')
    i += 1
