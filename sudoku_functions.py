import numpy as np


def print_sudoku(board):
    for i in board:
        for j in i:
            print(j.number, end=' ')
        print("\n")


def delete_from_domain(number, board, row, column):
    for r in board[:, column]:
        tmp = np.delete(r.domain, np.where(r.domain == number))
        r.domain = tmp
    for c in board[row, :]:
        tmp = np.delete(c.domain, np.where(c.domain == number))
        c.domain = tmp
    subgrid_row = row - row % 3
    subgrid_col = column - column % 3
    for i in range(3):
        for j in range(3):
            tmp = np.delete(board[subgrid_row + i][subgrid_col + j].domain,
                            np.where(board[subgrid_row + i][subgrid_col + j].domain == number))
            board[subgrid_row + i][subgrid_col + j].domain = tmp
    return board


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


def find_smallest_domain(board):
    mini = 9
    a = 0
    b = 0
    mini_a = 0
    mini_b = 0
    for i in board:
        for j in i:
            if j.number == 0:
                tmp = j.get_domain_size()
                # print(tmp, j.number)
                if tmp < mini:
                    mini = tmp
                    mini_a = a
                    mini_b = b
            a = (a + 1) % 9
        b = (b + 1) % 9

    return mini_b, mini_a


def update_first_domain(board):
    a = 0
    b = 0
    for i in board:
        for j in i:
            if j.number != 0:
                delete_from_domain(j.number, board, b, a)
            a = (a + 1) % 9
        b = (b + 1) % 9


def are_there_free_cells(board):
    for i in board:
        for j in i:
            if j == 0:
                return True
    return False


def check_if_in_domain(domain, number, r, c):
    # print("Checkin field", r, c, "is number ", number, "in domain ", domain)
    # print(r,c)
    # print("checking in domain", number, domain,)
    if number in domain:
        return True
    else:
        return False
