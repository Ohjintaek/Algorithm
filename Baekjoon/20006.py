import sys
input = sys.stdin.readline

p, m = map(int, input().split())
players = []
for _ in range(p):
    players.append(list(input().split()))

rooms = []
for i in range(p):
    no_room = True
    for room in rooms:
        if room[1] < m and (room[0] >= int(players[i][0]) - 10 and room[0] <= int(players[i][0]) + 10):
            room[1] += 1
            room[2].append(i)
            no_room = False
            break
    if no_room:
        rooms.append([int(players[i][0]), 1, [i]])

for room in rooms:
    if room[1] == m:
        print("Started!")
    else:
        print("Waiting!")
    temp = []
    for index in room[2]:
        temp.append(players[index])
    temp.sort(key=lambda x : x[1])
    for sorted_player in temp:
        print(sorted_player[0], sorted_player[1], sep = ' ')