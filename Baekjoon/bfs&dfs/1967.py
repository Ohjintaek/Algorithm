import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(start, distance):
    for child, value in tree[start]:
        if visited[child] == -1:
            visited[child] = distance + value
            dfs(child, visited[child])

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, value = map(int, input().split())
    tree[parent].append([child, value])
    tree[child].append([parent, value])

visited = [-1]*(n+1)
visited[0] = 0
dfs(1, 0)

startNode = visited.index(max(visited))
visited = [-1]*(n+1)
visited[startNode] = 0
dfs(startNode, 0)
print(max(visited))