import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

new_B = deque([])
for i in range(N):
    if A[i] == 0:
        new_B.append(B[i])

answer = []
for number in C:
    new_B.appendleft(number)
    answer.append(new_B.pop())

print(*answer)