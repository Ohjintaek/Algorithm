import sys
input = sys.stdin.readline
answer, row, col = 0, 1, 1

for i in range(9):
    numbers = list(map(int, input().split()))
    for j in range(9):
        if numbers[j] > answer:
            answer = numbers[j]
            row, col = i+1, j+1

print(answer)
print(row, col, sep = " ")