import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def dfs(now, weight):
    if (now == end):
        return True
    
    for edge in roads[now]:
        if (roads[now][edge] >= weight) and not visited[edge]:
            visited[edge] = True
            if dfs(edge, weight):
                True
    
    return False
    
N, M = map(int, input().split())
roads = [dict() for i in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    if (B in roads[A]):
        roads[A][B] = max(roads[A][B], C)
        roads[B][A] = roads[A][B]
    else:
        roads[A][B] = C
        roads[B][A] = C

start, end = map(int, input().split())

left, right = 1, 1000000000
while (left <= right):
    mid = (left+right) // 2
    visited = [False]*(N+1)
    visited[start] = True
    if (dfs(start, mid)):
        left = mid + 1
    else:
        right = mid - 1

print(right)