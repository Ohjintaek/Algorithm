import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map = []
for _ in range(N):
    map.append(input().strip())

boolean_map = [[False for _ in range(M)] for _ in range(N)]

map_set = set()
for i in range(N):
    for j in range(M):
        map_set.add((i,j))

answer = 0
while(map_set):
    position = map_set.pop()
    boolean_map[position[0]][position[1]] = True
    visited = [position]
    while True:
        direction = map[position[0]][position[1]]
        if direction == 'D':
            position = (position[0]+1, position[1])
            if boolean_map[position[0]][position[1]]:
                break
            else:
                boolean_map[position[0]][position[1]] = True
                visited.append(position)
                map_set.remove(position)

        elif direction == 'U':
            position = (position[0]-1, position[1])
            if boolean_map[position[0]][position[1]]:
                break
            else:
                boolean_map[position[0]][position[1]] = True
                visited.append(position)
                map_set.remove(position)

        elif direction == 'L':
            position = (position[0], position[1]-1)
            if boolean_map[position[0]][position[1]]:
                break
            else:
                boolean_map[position[0]][position[1]] = True
                visited.append(position)
                map_set.remove(position)

        else:
            position = (position[0], position[1]+1)
            if boolean_map[position[0]][position[1]]:
                break
            else:
                boolean_map[position[0]][position[1]] = True
                visited.append(position)
                map_set.remove(position)
    if (position in visited):
        answer += 1

print(answer)