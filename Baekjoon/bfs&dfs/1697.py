import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False]*100001

def bfs(pos):
    queue = deque([])
    queue.append(pos)
    visited[pos] = True

    cnt = 0
    while queue:
        if K in queue:
            return cnt
        tempq = deque([])
        for node in queue:
            if 0 <= node - 1 < 100001:
                if not visited[node-1]:
                    visited[node-1] = True
                    tempq.append(node-1)
            if node + 1 < 100001:
                if not visited[node+1]:
                    visited[node+1] = True
                    tempq.append(node + 1)
            if node*2 < 100001:
                if not visited[node*2]:
                    visited[node*2] = True
                    tempq.append(node*2)
        queue = tempq
        cnt += 1

print(bfs(N))