import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
orders = [[0, []] for _  in range(N+1)]
starts = set([i+1 for i in range(N)])
for _ in range(M):
    A, B = map(int, input().split())
    orders[B][0] += 1
    orders[A][1].append(B)
    starts.discard(B)

starts = deque(starts)
answer = []
while starts:
    person = starts.popleft()
    for next in orders[person][1]:
        orders[next][0] -= 1
        if orders[next][0] == 0:
            starts.append(next)
    answer.append(person)

print(*answer)