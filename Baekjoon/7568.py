import sys
input = sys.stdin.readline

N = int(input())
body = []
for _ in range(N):
    body.append(list(map(int, input().split())))

answer = []
for i in range(N):
    cnt = 1
    person = body[i]
    for j in range(N):
        if (person[0] < body[j][0]) and (person[1] < body[j][1]):
            cnt += 1
    answer.append(cnt)
    
print(*answer)