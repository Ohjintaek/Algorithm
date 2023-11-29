import sys
input = sys.stdin.readline

N, M = map(int, input().split())
flowers = [[-1 for _ in range(M+1)] for _ in range(N+1)]

left_flower = list(map(int, input().split()))
right_flower = list(map(int, input().split()))

for i in range(N):
    flowers[i+1][0] = left_flower[i]

for i in range(M):
    flowers[0][i+1] = right_flower[i]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (flowers[i][j-1] == flowers[i-1][j]):
            flowers[i][j] = 0
        else:
            flowers[i][j] = 1

print(flowers[N][M])
