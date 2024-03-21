import sys
input = sys.stdin.readline

T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))

dp = [0,1,2,4]

for i in range(1, 8):
    dp.append(dp[i] + dp[i+1] + dp[i+2])

for case in cases:
    print(dp[case])