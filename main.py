# Ex 39
import os
import shutil

# Список значений игрового поля
list_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Словарь для соответствия цифр Numpad индексам игрового поля
keys = {'7': 0, '8': 1, '9': 2, '4': 3, '5': 4, '6': 5, '1': 6, '2': 7, '3': 8}


# Функция отображения игрового поля 3х3
def show_game():
    """Показывает игровое поле в консоли"""
    os.system('cls')
    print('{{:-^{}}}'.format(shutil.get_terminal_size().columns).format('Крестики-нолики'))
    print(' {}  | {} | {} \n ----------- \n {}  | {} | {} \n ----------- \n {}  | {} | {}'.format(*list_board))


# Функция проверки игрового поля на предмет наличия ХХХ или ООО
def checking_values():
    """Проверяет игровое поле и возвращает победителя (Х или О)"""
    win_values = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [6, 5, 8], [2, 4, 6], [0, 4, 8]]
    for a, b, c in win_values:
        if list_board[a] == list_board[b] == list_board[c] and list_board[a] != ' ':
            return list_board[a]


# Логика BOTa
def make_a_first_move_bot():
    """Отвечает за первый ход компьютера"""
    if list_board[4] == 'X':
        list_board[0] = 'O'
    else:
        list_board[4] = 'O'


def make_a_second_move_bot():
    """Отвечает за второй ход компьютера"""
    if list_board[4] == 'X' and list_board[8] == 'X':
        list_board[2] = 'O'
    else:
        make_a_next_move_bot()


def checking_values_bot_O():
    """Проверяет стоят ли 2 'O' подряд и  возвращает индекс куда нужно поставить 'O' """
    win_values = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    for i in win_values:
        values = [list_board[j] for j in i]
        if values.count('O') == 2 and not values.count('X'):
            return i[(values.index(' '))]
    return -1


def checking_values_bot_X():
    """Проверяет стоят ли 2 'X' подряд и  возвращает индекс куда нужно поставить 'O' """
    win_values = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    for i in win_values:
        values = [list_board[j] for j in i]
        if values.count('X') == 2 and not values.count('O'):
            return i[(values.index(' '))]
    return list_board.index(' ')


def make_a_next_move_bot():
    """Отвечает за последующие ходы компьютера"""
    if checking_values_bot_O() == -1:
        list_board[checking_values_bot_X()] = 'O'
    else:
        list_board[checking_values_bot_O()] = 'O'


# Игровой процесс
def make_a_move():
    """Ввыставляет крестик в игровое поле в зависимости от введеного значения """
    count = 0
    show_game()
    while True:
        move = keys.get((input('\nСделайте ход: ')), 'False_') if not count % 2 else 'BOT'
        if move != 'False_' and move != 'BOT' and list_board[int(move)] == ' ':
            list_board[int(move)] = 'X'
            count += 1
            show_game()
            if checking_values():
                print('\nКонец игры! Победили', checking_values(), '!')
                break
            elif count == 9:
                print('\nКонец игры! Ничья!')
                break
        elif move == 'BOT':
            if count == 1:
                make_a_first_move_bot()
            elif count == 2:
                make_a_second_move_bot()
            else:
                make_a_next_move_bot()
            count += 1
            show_game()
            if checking_values():
                print('\nКонец игры! Победили', checking_values(), '!')
                break
            elif count == 9:
                print('\nКонец игры! Ничья!')
                break
        else:
            show_game()
            print('\nВведено неверное значение!')


if __name__ == '__main__':
    make_a_move()
