import sys
import heapq
input = sys.stdin.readline

def MST(start):
    _in = {start}
    edges = []
    for edge in graph[start]:
        heapq.heappush(edges, edge)

    result = 0
    size = 0
    while size < V-1:
        target = heapq.heappop(edges)
        if target[1] not in _in:
            _in.add(target[1])
            result += target[0]
            size += 1
            for edge in graph[target[1]]:
                heapq.heappush(edges, edge)

    return result

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

print(MST(1))