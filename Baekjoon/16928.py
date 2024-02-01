import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladders = dict()
snakes = dict()
for _ in range(N):
    key, value = map(int, input().split())
    ladders[key] = value
for _ in range(M):
    key, value = map(int, input().split())
    snakes[key] = value

graph = [[]]
for i in range(1, 100):
    temp = []
    for j in range(1,7):
        if i + j <= 100:
            if i+j in ladders:
                temp.append(ladders[i+j])
            elif i+j in snakes:
                temp.append(snakes[i+j])
            else:
                temp.append(i + j)
    graph.append(temp)

stack = deque([1])
visited = [False]*101
visited[1] = True

answer = 0
end = False
while(True):
    next = deque([])
    for position in stack:
        if position == 100:
            end = True
            break
        for candidate in graph[position]:
            if not visited[candidate]:
                next.append(candidate)
                visited[candidate] = True
    
    if end:
        break
    stack = next
    answer += 1

print(answer)