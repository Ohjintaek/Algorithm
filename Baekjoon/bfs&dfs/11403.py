import sys
input = sys.stdin.readline

def bfs(N, graph, start):
    queue = []
    visit = [False]*N
    queue.append(start)

    while queue:
        node = queue.pop()
        for i in range(N):
            if graph[node][i] == 1 and not visit[i]:
                queue.append(i)
                visit[i] = True
    
    return visit

N = int(input())
graph = []
for _  in range(N):
    graph.append(list(map(int, input().split())))

answer = [[0]*N for _ in range(N)]
for i in range(N):
    visit = bfs(N, graph, i)
    for j in range(N):
        if visit[j]:
            answer[i][j] = 1

for row in answer:
    print(*row)