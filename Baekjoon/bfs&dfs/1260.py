import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    fr, to = map(int, input().split())
    graph[fr].append(to)
    graph[to].append(fr)

for node in graph:
    node.sort()

def dfs(node):
    visited[node] = True
    print(node, end = ' ')
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

def bfs(node):
    queue = deque([])
    visited[node] = True
    queue.append(node)

    while queue:
        present = queue.popleft()
        print(present, end = ' ')
        for next in graph[present]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

visited = [False]*(N+1)
dfs(V)

print()

visited = [False]*(N+1)
bfs(V)