# random generation of a Catan board!
import random


def translate_to_text(board_list, rows):
    board_text = []
    text_list = ['desert', 'wheat', 'wood', 'sheep', 'brick', 'ore']
    for i in range(rows):
        board_text.append([])
    for i in range(rows):
        for j in range(len(board_list[i])):
            board_text[i].append(text_list[board_list[i][j]])
    return board_text


def new_board():
    reg_or_exp = input('Design a board for regular Catan (2-4 p) or Expansion (5-6 p)? Type reg or exp: ')
    # 0 = desert, 1 = wheat, 2 = wood, 3 = sheep, 4 = brick, 5 = ore
    # regular version has 19 tiles total, expansion has 30 tiles total
    if reg_or_exp == 'reg':
        tiles = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
        numbers_list = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        board = [[], [], [], [], []]
        row_lengths = [3, 4, 5, 4, 3]
        for i in range(5):
            while len(board[i]) < row_lengths[i]:
                tile = random.choice(tiles)
                board[i].append(tile)
                tiles.remove(tile)
        board_words = translate_to_text(board, 5)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board_words[i][j] != 'desert':
                    number = random.choice(numbers_list)
                    board_words[i][j] += f'-{number}'
                    numbers_list.remove(number)
        for i in range(5):
            print(board_words[i])

    if reg_or_exp == 'exp':
        tiles = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        numbers_list = [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12]
        board = [[], [], [], [], [], [], []]
        row_lengths = [3, 4, 5, 6, 5, 4, 3]
        for i in range(7):
            while len(board[i]) < row_lengths[i]:
                tile = random.choice(tiles)
                board[i].append(tile)
                tiles.remove(tile)
        board_words = translate_to_text(board, 7)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board_words[i][j] != 'desert':
                    number = random.choice(numbers_list)
                    board_words[i][j] += f'-{number}'
                    numbers_list.remove(number)
        for i in range(7):
            print(board_words[i])

    again = input('generate another board? (yes/no): ')
    if again == 'yes':
        new_board()
    else:
        exit()


new_board()
