import random

STRONG = 5040
# Максимальная сложность - количество вариантов,
# которые может обработать компьютер за 1 ход
# То есть максимально возможное (10х9х8х7 = 5040) кол-во вариантов


def get_all_answers():
    ans = []
    for _ in range(10000):
        tmp = str(_).zfill(4)
        lst = ['x' for num in tmp if tmp.count(num) == 1]
        if len(lst) == 4:
            ans.append(list(map(int, tmp)))
    return ans


def get_one_answer(ans):
    num = random.choice(ans)
    return num


def input_number():
    while True:
        nums = input('Введите 4 неповторяющиеся цифры: ')
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums


def check(nums, true_nums):
    bulls, cows = 0, 0
    for _, num in enumerate(nums):
        if num in true_nums:
            if nums[_] == true_nums[_]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def del_wrong_answers(ans, enemy_try, bull, cow):
    i = 0
    for num in ans[:]:
        i += 1
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
        #
        if i > STRONG:
        #
            break
    return ans


if __name__ == '__main__':
    STRONG = 300
    print('Игра Быки и коровы')
    answers = get_all_answers()
    player = input_number()
    enemy = get_one_answer(answers)

    while True:
        print('*' * 15, 'Ход игрока', '*' * 15)
        print('Угадайте число компьютера')
        number = input_number()
        bulls, cows = check(number, enemy)
        print('Быки: ', bulls, 'Коровы: ', cows)
        if bulls == 4:
            print(f'Победил игрок, верно угадав число компьютера: {enemy}')
            break

        print('*' * 15, 'Ход компьютера', '*' * 15)
        enemy_try = get_one_answer(answers)
        print('Думаю, вы загадали число', enemy_try)
        bulls, cows = check(enemy_try, player)
        print('Быки: ', bulls, 'Коровы: ', cows)
        if bulls == 4:
            print('Победил компьютер')
            print(f'Компьютер загадал: {enemy}')
            break
        else:
            answers = del_wrong_answers(answers, enemy_try, bulls, cows)
