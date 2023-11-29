import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
sq = [i + 1 for i in range(N)]
sq = deque(sq)

length = N
while length >= K:
    temp = sq.popleft()
    for _ in range(K-1):
        sq.popleft()
        length -= 1
    sq.append(temp)

print(sq[0])