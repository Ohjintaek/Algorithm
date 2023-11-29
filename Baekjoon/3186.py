import sys
input = sys.stdin.readline

K, L, N = map(int, input().split())
fee_time = input().strip()

answer = []
flag = False
waiting_time = 0

for i in range(N):
    if fee_time[i] == '1':
        if flag:
            waiting_time = 0
        else:
            waiting_time += 1
            if waiting_time >= K:
                flag = True
                waiting_time = 0
    else:
        if flag:
            waiting_time += 1
            if waiting_time >= L:
                answer.append(i + 1)
                flag = False
                waiting_time = 0
        else:
            waiting_time = 0

if flag:
    answer.append(N + L - waiting_time)

if len(answer) > 0:
    for time in answer:
        print(time)
else:
    print("NIKAD")