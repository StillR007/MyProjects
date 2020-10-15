with open('My_file_2.txt') as my_file:
    count_of_strings = len(my_file.readlines())
    print(f'В файле {count_of_strings} строк')
    my_file.seek(0)
    for line in my_file:
        print(f'{line}Здесь {len(line.split())} слов')
        # string = my_file.readline().split()
        # print(f'Слов в строке {1}: {len(list(string))}')
