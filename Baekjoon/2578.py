import sys
input = sys.stdin.readline

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))

column = [0 for _ in range(5)]
row = [0 for _ in range(5)]
left_diagonal = 0
right_diagonal = 0

bingo_count = 0
for n in range(25):
    flag = False
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == numbers[n]:
                flag = True
                break
        if flag:
            break
    column[i] += 1
    row[j] += 1
    if (i == j):
        right_diagonal += 1
    if (i + j == 4):
        left_diagonal += 1

    if (column[i] == 5):
        bingo_count += 1
    if (row[j] == 5):
        bingo_count += 1
    if (right_diagonal == 5):
        bingo_count += 1
        right_diagonal = 0
    if (left_diagonal ==5):
        bingo_count += 1
        left_diagonal = 0
    
    if bingo_count >= 3:
        print(n+1)
        break
    