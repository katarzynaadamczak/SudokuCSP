import pandas as pd
from sudoku import Sudoku
from Field import Field
import numpy as np


def read_sudoku(SOURCE_FILE):
    file = pd.read_csv(SOURCE_FILE, sep=";", skiprows=0)
    file = np.array(file)

    board = file[41][2]
    board1 = []
    row = 0

    for i in range(0, 81):
        col = i % 9
        if board[i] == '.':
            board1.append(Field(0, False, row, col))
        else:
            num = int(board[i])
            board1.append(Field(num, True, row, col))
        if col == 8:
            row += 1

    sudoku = np.reshape(np.array(board1), (9, 9))

    id = file[1][0]
    difficulty = file[1][1]

    return Sudoku(id, difficulty, sudoku)
