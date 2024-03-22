import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [0]*(sum(costs) + 1)
ans = 10000
for i in range(N):
    for j in range(sum(costs), costs[i]-1, -1):
        dp[j] = max(dp[j], dp[j-costs[i]] + memories[i])
        if dp[j] >= M and j < ans:
            ans = j

print(ans)