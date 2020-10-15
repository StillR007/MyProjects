def changing_language(string):
    words = {'One ': 'Один\n', 'Two ': 'Два\n', 'Three ': 'Три\n', 'Four ': 'Четыре\n'}
    with open('My_file_4_output.txt', 'a') as file_output:
        file_output.writelines(f'{number} - {words[string]}')


with open('My_file_4_input.txt') as file_input:
    for line in file_input:
        string, number = line.strip().split('-')
        changing_language(string)
print('Создн файл My_file_4_output.txt')
