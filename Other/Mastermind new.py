import random
import time


def round_history_player(*args):
    player_history.append([*args])
    return player_history


def round_history_comp(*args):
    comp_history.append([*args])
    return comp_history


def show_history():
    for round in player_history:
        print(f'{player_history.index(round)+1} ход: {round[0]}, быки: {round[1]}, коровы: {round[2]}')


def get_all_answers():
    ans = []
    for _ in range(10000):
        tmp = str(_).zfill(4)
        lst = ['x' for num in tmp if tmp.count(num) == 1]
        if len(lst) == 4:
            ans.append(list(map(int, tmp)))
    return ans


def choose_the_mode():
    while True:
        try:
            mode = int(input('Выберите режим игры:\n'
                             '1. Против компьютера\n'
                             '2. Против другого игрока на одном компьютере\n'
                             '3. По сети (сейчас недоступно)\n'))
        except (ValueError, NameError):
            pass
        if mode == 1:
            print('*' * 15, 'Игра против компьютера', '*' * 15)
        elif mode == 2:
            print('*' * 15, 'Против другого игрока на одном компьютере', '*' * 15)
        elif mode == 3:
            print('*' * 15, 'По сети (сейчас недоступно)', '*' * 15)
        else:
            continue
        return mode


def choose_the_level():
    while True:
        try:
            level = int(input('Выберите уровень сложности (цифру):\n'
                              '1. Легкий\n'
                              '2. Нормальный\n'
                              '3. Сложный\n'
                              '4. Очень сложный\n'
                              '5. Нереальный\n'))
        except (ValueError, NameError):
            pass
        if level == 1:
            strong = 150
            break
        elif level == 2:
            strong = 450
            break
        elif level == 3:
            strong = 700
            break
        elif level == 4:
            strong = 1200
            break
        elif level == 5:
            strong = 5040
            break
        else:
            print("Введите корректный уровень сложности!")
            continue
        return level, strong


def get_one_answer(ans):
    num = random.choice(ans)
    return num


def input_number():
    while True:
        nums = input('Введите 4 неповторяющиеся цифры: ')
        if nums == 'bcnjhbz' or nums == 'история':
            show_history()
            continue
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums


def check(comp_try, true_nums):
    bulls, cows = 0, 0
    for _, num in enumerate(comp_try):
        if num in true_nums:
            if comp_try[_] == true_nums[_]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def del_wrong_answers(ans, enemy_try, bull, cow):
    i = 0
    for num in ans[:]:
        i += 1
        if i >= strong:
            break
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans


global player_attempts
player_attempts = 0
global comp_attempts
comp_attempts = 0
global player_history
player_history = []
global comp_history
comp_history = []
global strong
strong = 0
global mode
mode = 0


if __name__ == '__main__':
    print('*' * 15, 'Игра Быки и коровы', '*' * 15)
    choose_the_mode()
    choose_the_level()
    all_answers = get_all_answers()
    player_number = input_number()
    enemy = get_one_answer(all_answers)

    while True:
        print('*' * 15, 'Ход игрока', '*' * 15, '\nУгадайте число компьютера',
              '\nЧтобы увидеть историю, введите "история"')
        player_try = input_number()
        bulls, cows = check(player_try, enemy)
        print('Быки: ', bulls, 'Коровы: ', cows)
        round_history_player(player_try, bulls, cows)
        if bulls == 4:
            print(f'Победил игрок за {len(round_history_player())} ходов')
            break

        print('*' * 15, 'Ход компьютера', '*' * 15)
        comp_try = get_one_answer(all_answers)
        time.sleep(0.5)
        print('Думаю, вы загадали число', comp_try)
        bulls, cows = check(comp_try, player_number)
        print('Быки: ', bulls, 'Коровы: ', cows)
        round_history_comp(comp_try, bulls, cows)
        if bulls == 4:
            print(f'Победил компьютер за {len(round_history_comp())} ходов', f'\nКомпьютер загадал: {enemy}')
            break
        else:
            answers = del_wrong_answers(all_answers, comp_try, bulls, cows)
