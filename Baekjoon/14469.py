import sys
input = sys.stdin.readline

N = int(input())
cows = []
for _ in range(N):
    cows.append(list(map(int, input().split())))

cows.sort(key=lambda x:x[0])

answer = 0
for cow in cows:
    if (answer < cow[0]):
        answer += (cow[0] - answer)
    answer += cow[1]

print(answer)