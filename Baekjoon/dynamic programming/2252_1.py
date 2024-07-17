import sys
import heapq
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

def getDP(node):
    if dp[node] > 0:
        return dp[node]
    else:
        result = 0
        for prev in orders[node]:
            result = max(result, getDP(prev))
        dp[node] = result + 1
        return dp[node]

N, M = map(int, input().split())
orders = [[] for _  in range(N+1)]
fronts = set([i+1 for i in range(N)])
for _ in range(M):
    A, B = map(int, input().split())
    orders[B].append(A)
    fronts.discard(B)

dp = [0]*(N+1)
for person in fronts:
    dp[person] = 1

answer = []
for i in range(1, N+1):
    heapq.heappush(answer, (getDP(i), i))

while answer:
    print(heapq.heappop(answer)[1], end = ' ')