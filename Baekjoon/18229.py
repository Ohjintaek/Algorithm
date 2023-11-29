import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
hands = []
for i in range(N):
    hands.append(list(map(int, input().split())))

people = [0 for _ in range(N)]
flag = False
for i in range(M):
    for j in range(N):
        people[j] += hands[j][i]
        if people[j] >= K:
            answer = j + 1
            count = i + 1
            flag = True
            break
    if flag:
        break

print(answer, count, sep = ' ')