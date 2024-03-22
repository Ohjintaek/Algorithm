import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N-i):
        if j == j+i:
            dp[j][j] = 1
            continue
        
        if numbers[j] == numbers[j+i]:
            if i == 1:
                dp[j][j+i] = 1
            else:
                if dp[j+1][j+i-1]:
                    dp[j][j+i] = 1

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])