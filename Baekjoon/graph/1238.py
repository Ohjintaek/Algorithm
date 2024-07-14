import sys
import heapq
input = sys.stdin.readline
INF = int(1e7)

def dijkstra(start, graph):
    times = [INF]*(N+1)
    minHeap = []
    heapq.heappush(minHeap, (0, start))
    times[start] = 0

    while minHeap:
        present = heapq.heappop(minHeap)
        for city, time in graph[present[1]]:
            if times[city] > present[0] + time:
                times[city] = present[0] + time
                heapq.heappush(minHeap, (times[city], city))
    
    return times


N, M, X = map(int, input().split())

forward = [[] for _ in range(N+1)]
backward = [[] for _  in range(N+1)]
for _ in range(M):
    fr, to, time = map(int, input().split())
    forward[fr].append([to, time])
    backward[to].append([fr, time])

go = dijkstra(X, forward)
back = dijkstra(X, backward)
answer = 0
for i in range(1, N+1):
    answer = max(answer, go[i] + back[i])

print(answer)