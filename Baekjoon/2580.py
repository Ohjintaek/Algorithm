import sys
input = sys.stdin.readline

def sudoku(board, n):
    if n == N:
        for numbers in board:
            print(*numbers)
        exit(0)
    for i in range(9):
        present = position[n]
        if isPossible(board, present, i+1):
            board[present[0]][present[1]] = i+1
            sudoku(board, n+1)
            board[present[0]][present[1]] = 0
        
def isPossible(board, position, candidate):
    for number in board[position[0]]:
        if number == candidate:
            return False
    for i in range(9):
        if board[i][position[1]] == candidate:
            return False
    for i in range(3):
        for j in range(3):
            if board[(position[0] // 3)*3 + i][(position[1] // 3)*3 + j] == candidate:
                return False
    return True

numbers = []
for _ in range(9):
    numbers.append(list(map(int, input().split())))

position = []
for i in range(9):
    for j in range(9):
        if numbers[i][j] == 0:
            position.append([i, j])
N = len(position)
sudoku(numbers, 0)