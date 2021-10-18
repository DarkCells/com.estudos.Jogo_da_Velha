# python 3.9.5 kubuntu

from IPython.display import clear_output


def display_board(board):
    clear_output()
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('-------------------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-------------------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
    print('-------------------')


display_board(" ", " ", " ", " ", " ", " ", " ", " ", " ")


def player_input():
    marker = ''
    while not (marker == 'x' or marker == "o"):
        marker = input('Player 1: Você quer ser X ou o ?').upper()

        if marker == 'x':
            return 'x', 'O'
        else:
            return '0', 'x'


def place_marker(board, marker, position):
    board[position] = marker


def win_check():
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or  # Vitória pelo topo
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # Vitória pelo meio
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # Vitória por baixo
            (board[7] == mark and board[4] == mark and board[7] == mark) or  # pelo esquerda
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # pelo meio
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # Vitória pela direita
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # vitória pela diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # Vitória pela diagonal


import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(0, 10):
        if space_check(boar, i):
            return False
        else:
            return True


def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha a sua jogada (1 - 9)')
    return int(position)


def replay():
    return input('Quer jogar novamente? "Sim" ou "Não" ').lower().startswith('s')


print('Bem vindo ao Jogo da Velha')
while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Começa!')

    game_on = True
    while game_on:
        # Vez do jogador 1
        if turn == 'Player1_marker':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
        # checagem de vitória
        if win_check(board, player1_marker):
            display_board(board)
            print('Parabéns! Você venceu')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 2'

        # vez do Jogador 2
        if turn == 'Player 2':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

        # Checagem vitória
        if win_check(board, player2_marker):
            display_board(board)
            print('Parabéns! Você venceu!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
            else:
                turn = 'Player 1'

    if not replay():
        break
