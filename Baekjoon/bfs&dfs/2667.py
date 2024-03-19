import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    houses = list(map(int, input().strip()))
    graph.append(houses)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = []
    queue.append([x,y])
    visited[x][y] = True

    cnt = 1
    while queue:
        next = queue.pop()
        for i in range(4):
            nx, ny = next[0] + dx[i], next[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    cnt +=1
    
    return cnt


visited = [[False]*N for _ in range(N)]

cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            ans.append(bfs(i, j))

print(cnt)
for num in sorted(ans):
    print(num)