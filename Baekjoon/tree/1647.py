import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    roads[A].append((C, B))
    roads[B].append((C, A))

added = [False]*(N+1)
maxRoad = 0
answer = 0

village = 1
added[village] = True
heap = []
count = 0
while count < N-1:
    for item in roads[village]:
        if not added[item[1]]:
            heapq.heappush(heap, item)
    
    while True:
        road, next = heapq.heappop(heap)
        if not added[next]:
            added[next] = True
            village = next
            answer += road
            maxRoad = max(maxRoad, road)
            count += 1
            break
    
print(answer - maxRoad)