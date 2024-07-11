import sys
input = sys.stdin.readline

def bfs(start, n, m, visit):
    queue = []
    queue.append(start)
    visit[start[0]][start[1]] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    distance = 1
    while queue:
        temp = []
        for pos in queue:
            x, y = pos[0], pos[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visit[nx][ny] == -1 and _map[nx][ny] == 1:
                        visit[nx][ny] = distance
                        temp.append([nx, ny])
        
        queue = temp
        distance += 1
    
    return visit

n, m = map(int, input().split())
_map = []
for i in range(n):
    _map.append(list(map(int, input().split())))

visit = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if _map[i][j] == 2:
            start = [i, j]
        if _map[i][j] == 0:
            visit[i][j] = 0

result = bfs(start, n, m, visit)
for row in result:
    print(*row)