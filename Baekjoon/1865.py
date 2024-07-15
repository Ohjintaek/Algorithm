import sys
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e7)

def bellmanFord(start):
    distance = [INF]*(N+1)
    distance[start] = 0

    for i in range(N):
        for key, value in edges.items():
            fr, to, time = key[0], key[1], value
            if distance[to] > distance[fr] + time:
                distance[to] = distance[fr] + time
                if i == N - 1:
                    return False
    return True

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = defaultdict(lambda: INF)
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges[(s, e)] = min(edges[(s, e)], t)
        edges[(e, s)] = min(edges[(e, s)], t)
        
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges[(s, e)] = min(edges[(s, e)], -t)

    if bellmanFord(1):
        print('NO')
    else:
        print('YES')