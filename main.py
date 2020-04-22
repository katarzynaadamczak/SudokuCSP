import pandas as pd
import numpy as np
import random
from read_sudoku_csv import read_sudoku
from sudoku import Sudoku
from Field import *
import time
from itertools import count
from sudoku_functions import update_first_domain, check_if_in_domain, delete_from_domain, print_sudoku, \
    find_smallest_domain

SOURCE_FILE = "Sudoku.csv"

global_board = 0
counter = 0


def main():
    task = read_sudoku(SOURCE_FILE)

    start = time.time()
    forwardchecking(task.board)
    # backtracking_without_domain_checking(task.board)
    stop = time.time()

    print_sudoku(global_board)
    # print_sudoku(task.board)
    print("Time:", stop - start)
    print("Nodes:", counter)


def forwardchecking(board):
    update_first_domain(board)
    forward_smallest_domain(board)


def forward_smallest_domain(board):
    l = [0, 0]
    if not find_unnasigned_field(board, l):
        global global_board
        global_board = board
        return True
    row, col = find_smallest_domain(board)

    global counter
    counter += 1

    for num in range(1, 10):
        if check_if_in_domain(board[row][col].domain, num, row, col):

            board[row][col].number = num
            tmp_board = copy_board(board)
            tmp_board = delete_from_domain(num, tmp_board, row, col)
            if forward_smallest_domain(tmp_board):
                return True
            board[row][col].number = 0
    return False


def copy_board(board):
    tmp = []
    for i in board:
        for j in i:
            new_field = Field(j.number, j.from_example, j.row, j.column)
            new_field.domain = np.copy(j.domain)
            tmp.append(new_field)
    tmp_board = np.reshape(np.array(tmp), (9, 9))
    return tmp_board


def backtracking_without_domain_checking(board):
    l = [0, 0]
    if not find_unnasigned_field(board, l):
        return True
    row = l[0]
    col = l[1]

    global counter
    counter += 1

    for num in range(1, 10):
        if number_is_approvable(num, board, row, col):
            board[row][col].number = num
            # print("Assigned ", num, "to field ", row, col)
            if backtracking_without_domain_checking(board):
                return True
            board[row][col].number = 0
    return False


def find_unnasigned_field(board, l):
    a = 0
    b = 0
    for i in board:
        for j in i:
            if j.number == 0:
                l[0] = b
                l[1] = a
                # print("Unnasigned position", l)
                return True
            a = (a + 1) % 9
        b = (b + 1) % 9
    # print_sudoku(board)
    return False


def number_is_approvable(number, board, row, col):
    for i in range(9):
        if board[row][i].number == number:
            return False
        if board[i][col].number == number:
            return False
    subgrid_row = row - (row % 3)
    subgrid_col = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if board[subgrid_row + i][subgrid_col + j].number == number:
                return False
    return True


main()
