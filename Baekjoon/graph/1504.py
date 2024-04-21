import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, N):
    visited = [False]*(N+1)
    cost = [1000000]*(N+1)

    queue = []
    heapq.heappush(queue, (0, start))
    cost[start] = 0

    while queue:
        node = heapq.heappop(queue)[1]
        if visited[node]:
            continue

        visited[node] = True
        for i in range(1, N+1):
            if visited[i] or length[node][i] == 0:
                continue

            cost[i] = min(cost[i], cost[node] + length[node][i])
            heapq.heappush(queue, (cost[i], i))
    
    return cost


N, E = map(int, input().split())

length = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    fr, to, v = map(int, input().split())
    length[fr][to] = v
    length[to][fr] = v

first, second = map(int, input().split())

startCost = dijkstra(1, N)
firstCost = dijkstra(first, N)
secondCost = dijkstra(second, N)

if startCost[N] >= 1000000 or startCost[first] >= 1000000 or startCost[second] >= 1000000:
    print(-1)
elif firstCost[second] >= 1000000:
    print(startCost[first] + startCost[second] + min(firstCost[N], secondCost[N]))
else:
    print(firstCost[second] + min(startCost[first] + secondCost[N], startCost[second] + firstCost[N]))