import Mastermind

answers = Mastermind.get_all_answers()
counter = 0
while len(answers) != 1:
    counter += 1
    print(f'Ход номер {counter}')
    print(f'Возможных вариантов ответа: {len(answers)}')
    ans = Mastermind.get_one_answer(answers)
    print('Назови комбинацию: ', ans)
    bulls = int(input('Сколько быков?'))
    if bulls == 4:
        break
    cows = int(input('Сколько коров?'))
    answers = Mastermind.del_wrong_answers(answers, ans, bulls, cows)
print('Ответ: ', answers)
