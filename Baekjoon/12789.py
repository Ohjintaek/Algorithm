import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
people = deque(list(map(int, input().split())))
wait = deque([N+1])

answer = "Nice"
present_number = 1
for _ in range(N):
    if wait[-1] == present_number:
        wait.pop()
        present_number += 1
        continue
    number = people.popleft()
    if number == present_number:
        present_number += 1
        continue
    if number < wait[-1]:
        wait.append(number)
    else:
        answer = "Sad"
        break
print(answer)