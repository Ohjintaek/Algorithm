targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

answer = 1
targets.sort(key = lambda x : x[0])
targets.sort(key = lambda x : x[1])

x_coord = targets[0][1]
for target in targets:
    if target[0] < x_coord:
        continue
    x_coord = target[1]
    answer += 1

print(answer)