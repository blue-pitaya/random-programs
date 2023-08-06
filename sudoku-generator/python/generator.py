#!/bin/env python3

board = [[0 for i in range(9)] for j in range(9)]

def check(row, col):
    n = board[row][col]
    # row
    for i in range(9):
        if i != col and board[row][i] == n:
            return False
    # col
    for i in range(9):
        if i != row and board[i][col] == n:
            return False
    # grid
    grid_row = row // 3
    grid_col = col // 3
    for r in range(3):
        for c in range(3):
            real_row = grid_row * 3 + r
            real_col = grid_col * 3 + c
            if real_row != row and real_col != col and board[real_row][real_col] == n:
                return False

    return True

def show():
    for row in board:
        print(row)

def to_pos(ptr):
    return (ptr // 9, ptr % 9)

stack = [0 for i in range(81)]
ptr = 0
limit = 1000000

for iter in range(limit):
    stack[ptr] += 1
    current = stack[ptr]
    row, col = to_pos(ptr)

    if current > 9:
        board[row][col] = 0
        stack[ptr] = 0
        ptr -= 1
        continue

    board[row][col] = stack[ptr]
    if check(row, col):
        if ptr+1 < 81:
            ptr += 1
        else:
            print(iter+1)
            show()
