import sys
input = sys.stdin.readline

N, L = map(int, input().split())
wholes = list(map(int, input().split()))
wholes.sort()

answer = 1
present = wholes[0]
for whole in wholes:
    if whole - present >= L:
        answer += 1
        present = whole

print(answer)