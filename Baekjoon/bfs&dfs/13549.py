import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False]*100001

def bfs(queue):
    cnt = 0
    while queue:
        tempq = deque([])
        for node in queue:
            if node == K:
                return cnt
            if 0 <= node - 1 < 100001:
                if not visited[node-1]:
                    visited[node-1] = True
                    tempq.append(node-1)
            if node + 1 < 100001:
                if not visited[node+1]:
                    visited[node+1] = True
                    tempq.append(node + 1)
        
        nextq = deque([])
        for node in tempq:
            nextq.append(node)
            pos = node
            while True:
                if not visited[pos]:
                    visited[pos] = True
                    nextq.append(pos)
                pos *= 2
                if 0 < pos <= 100000:
                    continue
                else:
                    break
        
        queue = nextq
        cnt += 1

start = deque([])
pos = N

while True:
    visited[pos] = True
    start.append(pos)
    pos *= 2

    if 0 < pos <= 100000:
        continue
    else:
        break

print(bfs(start))