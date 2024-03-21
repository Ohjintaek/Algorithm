import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

dp = [0]*N
for i in range(N):
    dp[i] = max(dp[i], P[i])
    for j in range(i+1, N):
        dp[j] = max(dp[j], dp[j-(i+1)] + P[i])

print(dp[N-1])