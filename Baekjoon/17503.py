import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())

beers = []
for _ in range(K):
    beers.append(list(map(int, input().split())))

beers.sort(key = lambda x : x[1])

beer_list = []
priority = 0
answer = beers[N-1][1]

for beer in beers[:N]:
    heapq.heappush(beer_list, beer[0])
    priority += beer[0]

if (priority >= M):
    print(answer)

else:
    index = N
    while priority < M:
        if (index >= K):
            break

        if (beer_list[0] < beers[index][0]):
            priority -= heapq.heappop(beer_list)
            priority += beers[index][0]
            heapq.heappush(beer_list, beers[index][0])
            answer = beers[index][1]
        index += 1
    
    if (priority >= M):
        print(answer)
    else:
        print(-1)