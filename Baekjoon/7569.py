import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    boxes.append(temp)

visited = [[[False]*M for _ in range(N)] for _ in range(H)]
stack = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                stack.append([j, k, i])
                visited[i][j][k] = True

cnt = -1
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
while(stack):
    next = deque([])
    for position in stack:
        for i in range(6):
            nx = position[0] + dx[i]
            ny = position[1] + dy[i]
            nz = position[2] + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if not visited[nz][nx][ny]:
                    if boxes[nz][nx][ny] == 0:
                        next.append([nx, ny, nz])
                        boxes[nz][nx][ny] = 1
                    visited[nz][nx][ny] = True
    stack = next
    cnt += 1

flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                flag = True

if flag:
    print(-1)
else:
    print(cnt)