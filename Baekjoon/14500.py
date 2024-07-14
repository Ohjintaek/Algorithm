import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    for j in range(M-1):
        seed = numbers[i][j] + numbers[i][j+1]
        branches = []
        if i > 0:
            branches.append(numbers[i-1][j])
            branches.append(numbers[i-1][j+1])
        if i < N-1:
            branches.append(numbers[i+1][j])
            branches.append(numbers[i+1][j+1])
        if j > 0:
            branches.append(numbers[i][j-1])
        if j < M-2:
            branches.append(numbers[i][j+2])
        branches.sort(reverse=True)
        tempSum = seed + branches[0] + branches[1]
        answer = max(answer, tempSum)

for i in range(N-1):
    for j in range(M):
        seed = numbers[i][j] + numbers[i+1][j]
        branches = []
        if i > 0:
            branches.append(numbers[i-1][j])
        if i < N - 2:
            branches.append(numbers[i+2][j])
        if j > 0:
            branches.append(numbers[i][j-1])
            branches.append(numbers[i+1][j-1])
        if j < M-1:
            branches.append(numbers[i][j+1])
            branches.append(numbers[i+1][j+1])
        branches.sort(reverse=True)
        tempSum = seed + branches[0] + branches[1]
        answer = max(answer, tempSum)

print(answer)