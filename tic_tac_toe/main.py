# Создайте программу для игры в "Крестики-нолики".
import emoji
import os


def show_board(ttt: dict):
    os.system('cls')
    print(f' ____________________',
        '|      |      |      |',
        f'|  {ttt["7"]}  |  {ttt["8"]}  |  {ttt["9"]}  |',
        '|______|______|______|',
        '|      |      |      |',
        f'|  {ttt["4"]}  |  {ttt["5"]}  |  {ttt["6"]}  |',
        '|______|______|______|',
        '|      |      |      |',
        f'|  {ttt["1"]}  |  {ttt["2"]}  |  {ttt["3"]}  |',
        '|______|______|______|\n', sep='\n')

def game_win(ttt: dict):
    if ttt['7'] == ttt['8'] == ttt['9'] or\
        ttt['4'] == ttt['5'] == ttt['6'] or\
        ttt['1'] == ttt['2'] == ttt['3'] or\
        ttt['7'] == ttt['4'] == ttt['1'] or\
        ttt['8'] == ttt['5'] == ttt['2'] or\
        ttt['9'] == ttt['6'] == ttt['3'] or\
        ttt['7'] == ttt['5'] == ttt['3'] or\
        ttt['9'] == ttt['5'] == ttt['1']:
        return True
    else: return False
    
def main():    
    game_keys = [str(i) for i in range(1,10)]
    game_board = {i: str(i) + ' ' for i in game_keys}
    turn = True
    step = 0
    x = emoji.emojize(':heavy_multiplication_x: ', language='alias')
    o = emoji.emojize(':o:', language='alias')
    show_board(game_board)
    while step != 9 and not game_win(game_board):
        sign = x if turn else o
        while (move := input(f' Ходят {"крестики" if sign == x else "нолики"}: ')) not in game_keys:
            show_board(game_board)
        game_keys.remove(move)
        game_board[move] = f'\033[33m{sign}\033[0m'
        show_board(game_board)
        step += 1
        turn = not turn
    if game_win(game_board): 
        print(f'{"Крестики" if sign == x else "Нолики"} победили!!\n')
    else: print('Ничья!\n')
    
if __name__ == '__main__':
    main()


