import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [dict() for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if v not in graph[u]:
        graph[u][v] = w
    else:
        graph[u][v] = min(graph[u][v], w)

visited = [False]*(V+1)
cost = [200000]*(V+1)

queue = []
heapq.heappush(queue, (0, K))
cost[K] = 0

while queue:
    node = heapq.heappop(queue)[1]
    if visited[node]:
        continue

    visited[node] = True
    for i in graph[node]:
        if visited[i]:
            continue

        cost[i] = min(cost[i], cost[node] + graph[node][i])
        heapq.heappush(queue, (cost[i], i))
    
for i in range(1, V+1):
    if cost[i] == 200000:
        print("INF")
    else:
        print(cost[i])