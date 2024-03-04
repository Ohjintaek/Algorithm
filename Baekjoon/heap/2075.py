import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(N-1):
    numbers = list(map(int, input().split()))
    for number in numbers:
        heapq.heappushpop(heap, number)

print(heapq.heappop(heap))
