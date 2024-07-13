import sys
input = sys.stdin.readline

def bfsGeneral(start, picture, N, visit):
    queue = []
    queue.append(start)
    visit[start[0]][start[1]] = True

    while queue:
        node = queue.pop()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx, ny = node[0]+dx[i], node[1]+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if picture[nx][ny] == picture[start[0]][start[1]] and not visit[nx][ny]:
                    queue.append([nx, ny])
                    visit[nx][ny] = True
    
    return visit

def bfsCB(start, picture, N, visit):
    queue = []
    queue.append(start)
    visit[start[0]][start[1]] = True

    while queue:
        node = queue.pop()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx, ny = node[0]+dx[i], node[1]+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if picture[start[0]][start[1]] == 'B':
                    if picture[nx][ny] == 'B' and not visit[nx][ny]:
                        queue.append([nx, ny])
                        visit[nx][ny] = True
                else:
                    if picture[nx][ny] != 'B' and not visit[nx][ny]:
                        queue.append([nx, ny])
                        visit[nx][ny] = True
    return visit

def findFalsePos(visit, N):
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                return [i, j]
    return False

N = int(input())
picture = []
for _ in range(N):
    picture.append(input().strip())

visit = [[False]*N for _ in range(N)]
general = 0
while findFalsePos(visit, N):
    general += 1
    bfsGeneral(findFalsePos(visit, N), picture, N, visit)

visit = [[False]*N for _ in range(N)]
CB = 0
while findFalsePos(visit, N):
    CB += 1
    bfsCB(findFalsePos(visit, N), picture, N, visit)

print(general, CB)