import sys
input = sys.stdin.readline

def mission(n, prev_location, prev_score):
    global answer
    if (prev_score >= M):
        answer += 6 ** (N-n)
        return
    if (n == N):
        return
    for i in range(6):
        if (i % 3 == prev_location):
            mission(n+1, i % 3, prev_score + score[i]/2)
        else:
            mission(n+1, i % 3, prev_score + score[i])    

N, M = map(int, input().split())
score = []
for _ in range(2):
    score.extend(list(map(int, input().split())))

answer = 0
mission(0, -1, 0)

print(answer)