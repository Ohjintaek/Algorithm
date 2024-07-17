import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

orders = [[0, []] for _ in range(N+1)]
for _ in range(M):
    _input = list(map(int, input().split()))
    for i in range(1, _input[0]):
        orders[_input[i]][1].append(_input[i+1])
        orders[_input[i+1]][0] += 1

queue = deque([])
for i in range(1, N+1):
    if orders[i][0] == 0:
        queue.append(i)

answer = []
length = 0
while queue:
    person = queue.popleft()
    for next in orders[person][1]:
        orders[next][0] -= 1
        if orders[next][0] == 0:
            queue.append(next)
    
    answer.append(person)
    length += 1

if length == N:
    print('\n'.join(map(str, answer)))
else:
    print(0)