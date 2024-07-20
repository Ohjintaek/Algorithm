import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    visited = [False]*(N+1)
    costs = [INF]*(N+1)
    costs[start] = 0

    priorityQueue = [(costs[start], start)]
    while priorityQueue:
        cost, node = heapq.heappop(priorityQueue)
        if visited[node]:
            continue

        visited[node] = True
        for next in buses[node]:
            costs[next] = min(costs[next], cost+buses[node][next])
            if not visited[next]:
                heapq.heappush(priorityQueue, (costs[next], next))
        
    return costs


N = int(input())
M = int(input())

buses = [{i: 0} for i in range(N+1)]
for _ in range(M):
    fr, to, v = map(int, input().split())
    if to in buses[fr]:
        buses[fr][to] = min(buses[fr][to], v)
    else:
        buses[fr][to] = v

A, B = map(int, input().split())
costs = dijkstra(A)

print(costs[B])