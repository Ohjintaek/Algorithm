import sys
input = sys.stdin.readline
maxInteger = 2**31

N = int(input())
matrixSizes = []
for _ in range(N):
    matrixSizes.append(list(map(int, input().split())))

memoize = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(N):
        if i + j == N:
            break

        memoize[j][j+i] = maxInteger
        for k in range(j, j+i):
            memoize[j][j+i] = min(memoize[j][j+i], memoize[j][k] + memoize[k+1][j+i] + matrixSizes[j][0]*matrixSizes[k][1]*matrixSizes[j+i][1])

print(memoize[0][N-1])