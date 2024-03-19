import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomatos = []
for _ in range(N):
    tomatos.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = []
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            queue.append((i,j))

ans = -1
while queue:
    tempq = []
    for pos in queue:
        for i in range(4):
            nx, ny = pos[0] + dx[i], pos[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = 1
                    tempq.append((nx,ny))

    queue = tempq
    ans += 1

flag = False
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 0:
            flag = True

if flag:
    print(-1)
else:
    print(ans)