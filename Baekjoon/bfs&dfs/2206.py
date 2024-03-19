import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().strip())))

visited = [[[-1]*M for _ in range(N)] for _ in range(2)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(flag, x, y):
    queue = []
    queue.append([flag, x, y])
    visited[0][x][y] = 1
    visited[1][x][y] = 1

    while queue:
        tempq = []
        for pos in queue:
            if pos[1] == N-1 and pos[2] == M-1:
                return
            for i in range(4):
                nx, ny = pos[1] + dx[i], pos[2] + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if maps[nx][ny] == 0:
                        if visited[pos[0]][nx][ny] < 0:
                            tempq.append([pos[0], nx, ny])
                            visited[pos[0]][nx][ny] = visited[pos[0]][pos[1]][pos[2]] + 1
                    else:
                        if pos[0] == 0:
                            if visited[1][nx][ny] < 0:
                                tempq.append([1, nx, ny])
                                visited[1][nx][ny] = visited[pos[0]][pos[1]][pos[2]] + 1
        queue = tempq

bfs(0,0,0)
print(max(visited[0][N-1][M-1], visited[1][N-1][M-1]))