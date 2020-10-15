with open('My_file_1.txt', 'x+') as my_file:
    user_input = "something"
    while user_input:
        user_input = input('Введите данные')
        my_file.writelines(f'{user_input}\n')
