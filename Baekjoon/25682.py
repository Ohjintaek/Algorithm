import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = []
for i in range(N):
    board.append(input().strip())

count = [[0 for _ in range(M+1)] for _ in range(N+1)]

flag = True
for i in range(N):
    for j in range(M):
        if flag:
            if board[i][j] == 'B':
                count[i][j] = count[i-1][j] + count[i][j-1] - count[i-1][j-1]
            else:
                count[i][j] = 1 + count[i-1][j] + count[i][j-1] - count[i-1][j-1]
        else:
            if board[i][j] == 'B':
                count[i][j] = 1 + count[i-1][j] + count[i][j-1] - count[i-1][j-1]
            else:
                count[i][j] = count[i-1][j] + count[i][j-1] - count[i-1][j-1]
        flag = not flag
    if M % 2 == 0:
        flag = not flag

answer = K*K
for i in range(N-K+1):
    for j in range(M-K+1):
        tempAnswer = count[i+K-1][j+K-1] - count[i+K-1][j-1] - count[i-1][j+K-1] + count[i-1][j-1]
        tempAnswer = min(tempAnswer, K*K - tempAnswer)
        answer = min(answer, tempAnswer)

print(answer)