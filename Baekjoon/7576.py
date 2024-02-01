import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
boxes = []
for _ in range(N):
    boxes.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)]
stack = deque([])
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            stack.append([i, j])
            visited[i][j] = True

cnt = -1
dx, dy = [1, -1, 0, 0,], [0, 0, 1, -1]
while(stack):
    next = deque([])
    for position in stack:
        for i in range(4):
            nx = position[0] + dx[i]
            ny = position[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if boxes[nx][ny] == 0:
                        next.append([nx, ny])
                        boxes[nx][ny] = 1
                    visited[nx][ny] = True
    stack = next
    cnt += 1

flag = False
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 0:
            flag = True

if flag:
    print(-1)
else:
    print(cnt)