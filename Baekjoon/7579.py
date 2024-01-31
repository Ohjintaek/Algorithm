import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
costSum = sum(costs)

ans = 1e9
dp = [0]*(costSum+1)
for i in range(N):
    memory, cost = memories[i], costs[i]
    for j in range(costSum, cost-1, -1):
        dp[j] = max(dp[j], memory+dp[j-cost])
        if dp[j] >= M:
            ans = min(ans, j)
print(ans)