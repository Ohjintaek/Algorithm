import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

answer = itertools.product([i+1 for i in range(N)], repeat=M)

for i in answer:
    print(*i)