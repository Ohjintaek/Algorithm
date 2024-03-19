import sys
from collections import deque
input = sys.stdin.readline

def bfs(pos):
    queue = deque([])
    queue.append(pos)
    visited[pos] = True

    while queue:
        next = queue.popleft()
        for node in graph[next]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

N = int(input())
M = int(input())

graph = [set() for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

visited = [False]*(N+1)
bfs(1)

print(visited.count(True) - 1)