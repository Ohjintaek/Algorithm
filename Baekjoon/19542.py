import sys
from collections import deque
input = sys.stdin.readline

def dfs(n, d, graph, start):
    visited = [False]*n
    need_visited = deque()

    need_visited.append([start,0])
    
    answer = 0
    while need_visited:
        node = need_visited.pop()
        print(node)
        if not visited[node[0]]:
            visited[node[0]] = True
            flag = False
            for next in graph[node[0]]:
                if visited[next]:
                    continue
                need_visited.append([next, node[1]+1])
                flag = True
            if not flag:
                print(max(0, node[1]-d))
                answer += max(0, node[1]-d)

    return answer*2

N, S, D = map(int, input().split())

roads = []
for _  in range(N-1):
    roads.append(list(map(int, input().split())))

graph = [[] for _ in range(N)]

for node in roads:
    graph[node[0]-1].append(node[1]-1)
    graph[node[1]-1].append(node[0]-1)

answer = dfs(N, D, graph, S-1)
print(answer)