import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solution(row, col):
    if col == 9:
        row += 1
        col = 0
    if row == 9:
        return True
    
    if sudoku[row][col] != '0':
        return solution(row, col+1)
    else:
        for i in range(1, 10):
            if rowCondition[row][i] or colCondition[col][i] or boxCondition[(row//3)*3 + col//3][i]:
                continue

            rowCondition[row][i] = True
            colCondition[col][i] = True
            boxCondition[(row//3)*3 + col//3][i] = True
            sudoku[row][col] = str(i)
            
            if solution(row, col+1):
                return True
            
            rowCondition[row][i] = False
            colCondition[col][i] = False
            boxCondition[(row//3)*3 + col//3][i] = False
            sudoku[row][col] = '0'
    return False

sudoku = []
for _ in range(9):
    sudoku.append(list(input().strip()))

rowCondition = [[False]*10 for _ in range(9)]
colCondition = [[False]*10 for _ in range(9)]
boxCondition = [[False]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        target = int(sudoku[i][j])
        rowCondition[i][target] = True
        colCondition[j][target] = True
        boxCondition[(i//3)*3 + j//3][target] = True

solution(0, 0)
for i in range(9):
    print(''.join(sudoku[i]))