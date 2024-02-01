import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(input().strip())

stack = [[0, 0, False]]
visited = [[[False]*M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = True
visited[1][0][0] = True

answer = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
end = False
while(stack):
    next = []
    for position in stack:
        if position[0] == N-1 and position[1] == M-1:
            end = True
            break
        for i in range(4):
            nx = position[0] + dx[i]
            ny = position[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if position[2]:
                    if maps[nx][ny] == '0' and not visited[1][nx][ny]:
                        next.append([nx, ny, True])
                        visited[1][nx][ny] = True
                else:
                    if maps[nx][ny] == '0':
                        if not visited[0][nx][ny]:
                            next.append([nx, ny, False])
                            visited[0][nx][ny] = True
                    elif not visited[1][nx][ny]:
                        next.append([nx, ny, True])
                        visited[1][nx][ny] = True
    answer += 1
    if end:
        break
    stack = next

if visited[0][N-1][M-1] or visited[1][N-1][M-1]:
    print(answer)
else:
    print(-1)