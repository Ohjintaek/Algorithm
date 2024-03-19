import sys
import copy
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
init = []
for _ in range(N):
    init.append(list(map(int, input().split())))

def bfs(maps):
    queue = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                queue.append([i,j])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        tempq = []
        for pos in queue:
            for i in range(4):
                nx, ny = pos[0] + dx[i], pos[1] + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = 2
                        tempq.append([nx,ny])
        queue = tempq
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                cnt += 1
    return cnt

pool = []
for i in range(N):
    for j in range(M):
        pool.append([i,j])

candidates = itertools.combinations(pool, 3)

ans = 0
for candidate in candidates:
    maps = copy.deepcopy(init)
    flag = True
    for pos in candidate:
        if maps[pos[0]][pos[1]] == 0:
            maps[pos[0]][pos[1]] = 1
        else:
            flag = False
            break
    if flag:
        ans = max(ans, bfs(maps))

print(ans)