import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    classes.append(list(map(int, input().split())))
classes.sort(key = lambda x : x[0])

answer = []
heapq.heappush(answer, classes[0][1])
for i in range(1,N):
    if classes[i][0] < answer[0]:
        heapq.heappush(answer, classes[i][1])
    else:
        heapq.heappushpop(answer, classes[i][1])

print(len(answer))
