import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(start, visited, group):
    visited[start] = group

    for pos in graph[start]:
        if visited[pos] == 0:
            result = dfs(pos, visited, -group)
            if not result:
                return False
        else:
            if visited[pos] == group:
                return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        fr, to = map(int, input().split())
        graph[fr].append(to)
        graph[to].append(fr)

    for i in range(1, V+1):
        if visited[i] == 0:
            answer = dfs(i, visited, 1)
            if not answer:
                break
    
    if answer:
        print("YES")
    else:
        print("NO")