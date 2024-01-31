import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
maps = []
for _ in range(M):
    maps.append(list(map(int, input().split())))

dp = [[-1]*N for _ in range(M)]

def dfs(a, b):
    if a == M-1 and b == N-1:
        return 1
    if dp[a][b] != -1:
        return dp[a][b]
    
    dp[a][b] = 0
    if a > 0:
        if maps[a][b] > maps[a-1][b]:
            dp[a][b] += dfs(a-1, b)
    if a < M-1:
        if maps[a][b] > maps[a+1][b]:
            dp[a][b] += dfs(a+1, b)
    if b > 0:
        if maps[a][b] > maps[a][b-1]:
            dp[a][b] += dfs(a, b-1)
    if b < N-1:
        if maps[a][b] > maps[a][b+1]:
            dp[a][b] += dfs(a, b+1)
    return dp[a][b]

print(dfs(0,0)) 