import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split())))

bags = []
for _ in range(K):
    bags.append(int(input()))

# 제일 가벼운 가방부터 넣을 수 있는 최대 가치의 보석을 차례로 넣는다.
bags.sort()

answer = 0
jewelWeightHeap = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        jewel = heapq.heappop(jewels)
        heapq.heappush(jewelWeightHeap, -jewel[1])
    answer += -heapq.heappop(jewelWeightHeap)

print(answer)