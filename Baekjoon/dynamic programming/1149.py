import sys
input = sys.stdin.readline

N = int(input())

expenses = []
for _ in range(N):
    expenses.append(list(map(int, input().split())))

dp = [[0,0,0]]
for expense in expenses:
    prev = dp[-1]
    red = min(prev[1], prev[2]) + expense[0]
    green = min(prev[0], prev[2]) + expense[1]
    blue = min(prev[0], prev[1]) + expense[2]
    dp.append([red,green,blue])

print(min(dp[N]))