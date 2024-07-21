import sys
import heapq
input = sys.stdin.readline

def bfs(start, size):
    visited = [[False]*N for _ in range(N)]
    queue = []
    visited[start[0]][start[1]] = True
    queue.append(start)

    distance = 0
    while queue:
        temp = []
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while queue:
            node = heapq.heappop(queue)
            if 0 < space[node[0]][node[1]] < size:
                space[node[0]][node[1]] = 0
                return (node, distance)
            
            for i in range(4):
                nx, ny = node[0]+dx[i], node[1]+dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if space[nx][ny] > size:
                        continue

                    visited[nx][ny] = True
                    heapq.heappush(temp, [nx, ny])

        queue = temp
        distance += 1
        
    return (sharkPosition, 0)


N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            sharkPosition = [i, j]
            space[i][j] = 0

answer = 0
size = 2
toIncrease = size
while True:
    sharkPosition, time = bfs(sharkPosition, size)
    if time == 0:
        break

    answer += time
    toIncrease -= 1
    if toIncrease == 0:
        size += 1
        toIncrease = size

print(answer)