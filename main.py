board_size = 3

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

MODE_HUMAN_VS_HUMAN = '1'
MODE_HUMAN_VS_AI = '2'


def draw_board():
    print(('_' * 4 * board_size))
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)


def check_win(board):
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X', 'O')):
            win = board[pos[0]]

    return win


def game_step(index, char):
    if (index > 10 or index < 1 or board[index - 1] in ('X', 'O')):
        return False

    board[index - 1] = char
    return True

def computer_step(human, ai):
    available_steps = [i - 1 for i in board if type(i) == int]
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    for char in (ai, human):
        for pos in available_steps:
            board_ai = board[:]
            board_ai[pos] = char
            if (check_win(board_ai) != False):
                return pos

    for pos in win_steps:
        if (pos in available_steps):
            return pos

    return False


def next_player(current_player):
    if (current_player == 'X'):
        return 'O'

    return 'X'


def start_game(mode):
    current_player = 'X'
    ai_player = 'O'
    step = 1

    draw_board()

    while (step < 9) and (check_win(board) == False):
        index = input('Ходит ' + current_player + '. Введите номер поля (0 - выход):')

        if (int(index) == 0):
            break

        if (game_step(int(index), current_player)):
            print('Удачный ход')
            current_player = next_player(current_player)
            step += 1

            if (mode == MODE_HUMAN_VS_AI):
                if (computer_step('X', 'O') != False):
                    board[computer_step('X', 'O')] = ai_player
                    current_player = next_player(current_player)
                    step += 1

            draw_board()

        else:
            print('Неверный номер! Повторите!')

    if (step > 8):
        print('Игра окончена. Ничья!')
    elif check_win(board):
        print('Выиграл ' + check_win(board))


print('Приветствуем Вас в игре "Крестики нолики" !')
mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
    mode = input("Режим игры:\n1 - Человек против Человека\n2 - Человек против Компьютер\nВыберите режим игры:")

start_game(mode)
