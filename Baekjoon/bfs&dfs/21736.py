import sys
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
for _ in range(N):
    campus.append(input().strip())

def bfs(pos, campus):
    queue = []
    visit = [[False for _ in range(M)] for _ in range(N)]
    queue.append(pos)
    visit[pos[0]][pos[1]] = True
    result = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        node = queue.pop()
        x, y = node[0], node[1]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if campus[nx][ny] != 'X' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append([nx, ny])
                    if campus[nx][ny] == 'P':
                        result += 1
    
    return result

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = [i, j]

result = bfs(start, campus)
if result == 0:
    print('TT')
else:
    print(result)