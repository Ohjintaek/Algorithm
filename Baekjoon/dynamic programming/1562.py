import sys
input = sys.stdin.readline

N = int(input())
dp = [[[0]*(1<<10) for _ in range(10)] for _ in range(N+1)]

for i in range(10):
    dp[1][i][1<<i] = 1
dp[1][0][1] = 0

for i in range(1, N):
    for j in range(10):
        for k in range(1<<10):
            if j > 0:
                dp[i+1][j-1][k | 1<<(j-1)] += dp[i][j][k]
            if j < 9:
                dp[i+1][j+1][k | 1<<(j+1)] += dp[i][j][k]
                
answer = 0
for i in range(10):
    answer += dp[N][i][(1<<10)-1]

print(answer % 1000000000)