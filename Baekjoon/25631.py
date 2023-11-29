import sys
input = sys.stdin.readline

N = int(input())
dolls = list(map(int, input().split()))

dolls.sort()

temp = 0
answer = 1
temp_answer = 0

for doll in dolls:
    if doll == temp:
        temp_answer += 1
        continue
    answer = max(answer, temp_answer)
    temp_answer = 1
    temp = doll

answer = max(answer, temp_answer)

print(answer)