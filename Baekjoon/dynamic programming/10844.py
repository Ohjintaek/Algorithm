import sys
input = sys.stdin.readline

N = int(input())

dp = [[0,1,1,1,1,1,1,1,1,1]]
for i in range(1, N):
    tmp = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        if i >= 1:
            tmp[i-1] += dp[-1][i]
        if i < 9:
            tmp[i+1] += dp[-1][i]
    dp.append(tmp)

print(sum(dp[N-1]) % 1000000000)