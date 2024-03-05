import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

grounds = []
for _ in range(N):
    grounds.extend(list(map(int, input().split())))
grounds.sort(reverse=True)
min_height = grounds[-1]
max_height = grounds[0]

answer_time = 500*500*256*2
answer_height = min_height
for i in range(min_height, max_height + 1):
    time = 0
    remain = B
    flag = True
    for j in range(N*M):
        if grounds[j] > i:
            diff = grounds[j] - i
            time += 2*diff
            remain += diff
        else:
            diff = i - grounds[j]
            time += diff
            remain -= diff
        if remain < 0 or time > answer_time:
            flag = False
            break
    if flag:
        if time < answer_time:
            answer_time = time
            answer_height = i
        elif time == answer_time:
            if answer_height < i:
                answer_height = i

print(answer_time, answer_height)