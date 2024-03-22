import sys
input = sys.stdin.readline

N, M = map(int, input().split())
shelters = list(map(int, input().split()))
shelterIndex = []
for i in range(N):
    shelterIndex.append([shelters[i], i+1])
shelterIndex.sort(key = lambda x : -x[0])

roads = [[] for _ in range(N+1)]
for _ in range(M):
    fr, to = map(int, input().split())
    roads[fr].append(to)
    roads[to].append(fr)

dp = [0]*(N+1)
def dfs(pos, cnt):
    for child in roads[pos]:
        if shelters[child-1] <= shelters[pos-1]:
            continue

        if dp[child] != 0:
            dp[pos] = max(dp[pos], cnt + dp[child])
        else:
            dp[pos] = dfs(child, cnt+1)
        
    dp[pos] = max(dp[pos], cnt)
    return dp[pos]

for i in range(N):
    dfs(shelterIndex[i][1], 1)

for i in range(1, N+1):
    print(dp[i])