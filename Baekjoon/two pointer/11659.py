import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

prefixSum = [0]
for num in numbers:
    prefixSum.append(prefixSum[-1] + num)

for _ in range(M):
    fr, to = map(int, input().split())
    print(prefixSum[to] - prefixSum[fr-1])
