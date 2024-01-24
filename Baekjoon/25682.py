import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = []
for i in range(N):
    board.append(input().strip())

count = []
for i in range(N):
    startB = [0]
    startW = [0]
    flag = True
    for j in range(M):
        if flag:
            if board[i][j] != 'B':
                startB.append(startB[-1] + 1)
                startW.append(startW[-1])
            else:
                startW.append(startW[-1] + 1)
                startB.append(startB[-1])
        else:
            if board[i][j] == 'B':
                startB.append(startB[-1] + 1)
                startW.append(startW[-1])
            else:
                startW.append(startW[-1] + 1)
                startB.append(startB[-1])
        flag = not flag
    count.append([startB, startW])

answer = K*K
for i in range(N-K+1):
    for j in range(M-K+1):
        startB, startW = 0, 0
        flag = 0
        for k in range(K):
            nextFlag = (flag+1) % 2
            startB += count[i+k][flag][K+j] - count[i+k][flag][j]
            startW += count[i+k][nextFlag][K+j] - count[i+k][nextFlag][j]
            flag = nextFlag
        answer = min(answer, min(startB, startW))
print(answer)