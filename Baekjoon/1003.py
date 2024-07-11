import sys
input = sys.stdin.readline

dp = [[1, 0], [0, 1]]
for i in range(2, 41):
    count0 = dp[i-2][0] + dp[i-1][0]
    count1 = dp[i-2][1] + dp[i-1][1]
    dp.append([count0, count1])

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])