import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 1, 2]

for _ in range(n - 2):
    dp.append((dp[-1] + dp[-2]) % 10007)

print(dp[n])