import sys
input = sys.stdin.readline

board = []
for _ in range(10):
    board.append(input().strip())

flag = False
for i in range(10):
    if flag:
        break
    for j in range(6):
        temp_board = board[i][j:j+5]
        if (temp_board.count('X') == 4 and temp_board.count('O') == 0):
            print(1)
            flag = True
            break

for i in range(10):
    if flag:
        break
    temp_board = []
    for j in range(10):
        temp_board.append(board[j][i])

    for j in range(6):
        temp = temp_board[j:j+5]
        if (temp.count('X') == 4 and temp.count('O') == 0):
            print(1)
            flag = True
            break

for i in range(6):
    if flag:
        break
    temp_board = []
    for j in range(10 - i):
        temp_board.append(board[j][i+j])

    for j in range(len(temp_board) - 4):
        temp = temp_board[j:j+5]
        if (temp.count('X') == 4 and temp.count('O') == 0):
            print(1)
            flag = True
            break

for i in range(1, 6):
    if flag:
        break
    temp_board = []
    for j in range(10 - i):
        temp_board.append(board[i+j][j])

    for j in range(len(temp_board) - 4):
        temp = temp_board[j:j+5]
        if (temp.count('X') == 4 and temp.count('O') == 0):
            print(1)
            flag = True
            break

for i in range(6):
    if flag:
        break
    temp_board = []
    for j in range(10 - i):
        temp_board.append(board[j][9-j-i])

    for j in range(len(temp_board) - 4):
        temp = temp_board[j:j+5]
        if (temp.count('X') == 4 and temp.count('O') == 0):
            print(1)
            flag = True
            break

for i in range(1, 6):
    if flag:
        break
    temp_board = []
    for j in range(10 - i):
        temp_board.append(board[i+j][9-j])

    for j in range(len(temp_board) - 4):
        temp = temp_board[j:j+5]
        if (temp.count('X') == 4 and temp.count('O') == 0):
            print(1)
            flag = True
            break

if not flag:
    print(0)