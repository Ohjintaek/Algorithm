import sys
import heapq
input = sys.stdin.readline

N, M, k = map(int, input().split())

friend_fee = list(map(int, input().split()))

relationships = []
for _ in range(M):
    relationships.append(list(map(int, input().split())))

friends = [set() for _ in range(N)]
visited = [False]*N

for relation in relationships:
    friends[relation[0]-1].add(relation[1]-1)
    friends[relation[1]-1].add(relation[0]-1)

total_fee = 0

while False in visited:
    index = visited.index(False)
    graph = friends[index]
    visited[index] = True
    fee_heap = []
    heapq.heappush(fee_heap, friend_fee[index])
    while graph:
        node = graph.pop()
        if not visited[node]:
            graph.update(friends[node])
            visited[node] = True
            heapq.heappush(fee_heap, friend_fee[node])
    total_fee += heapq.heappop(fee_heap)
    fee_heap = []

if (total_fee <= k):
    print(total_fee)
else:
    print("Oh no")