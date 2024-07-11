import sys
input = sys.stdin.readline

dp = [1, 1]
for i in range(2, 251):
    dp.append(dp[i-1] + dp[i-2]*2)

while True:
    n = input()
    if not n:
        break

    print(dp[int(n)])