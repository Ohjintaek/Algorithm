import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [set() for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

visited = [False]*N

def bfs(pos):
    queue = deque([])
    queue.append(pos)
    visited[pos-1] = True

    while(queue):
        next = queue.popleft()
        for child in graph[next]:
            if not visited[child-1]:
                visited[child-1] = True
                queue.append(child)

cnt = 0
while False in visited:
    pos = visited.index(False) + 1
    bfs(pos)
    cnt += 1

print(cnt)