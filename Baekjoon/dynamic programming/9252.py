import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

dp = [['' for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i+1][j+1] = dp[i][j] + A[i]
        else:
            if len(dp[i+1][j]) > len(dp[i][j+1]):
                dp[i+1][j+1] = dp[i+1][j]
            else:
                dp[i+1][j+1] = dp[i][j+1]

length = len(dp[i+1][j+1])
print(length)
if length > 0:
    print(dp[i+1][j+1])