def changing_letter():
    print(user_answer.capitalize())


def changing_letters():
    print(user_answer.title())


user_answer = input('Введите слово из латинских букв или слова через пробел')
if len(user_answer) > 1:
    changing_letters()
elif len(user_answer) == 0:
    print('Вы ничего не ввели!')
elif user_answer is not str:
    print('Это не слова!')
else:
    changing_letter()
