import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(start, distance):
    for node in tree[start]:
        if visited[node] == -1:
            visited[node] = distance + tree[start][node]
            dfs(node, visited[node])

V = int(input())
tree = [dict() for _ in range(V+1)]
leafNodes = []
for _ in range(V):
    data = list(map(int, input().split()))
    n = len(data)
    if n == 4:
        leafNodes.append(data[0])

    for i in range(1, n - 2, 2):
        to, value = data[i], data[i+1]
        tree[data[0]][to] = value
        tree[to][data[0]] = value

visited = [-1]*(V+1)
visited[leafNodes[0]] = 0
dfs(leafNodes[0], 0)
startNode = visited.index(max(visited))

visited = [-1]*(V+1)
visited[startNode] = 0
dfs(startNode, 0)
print(max(visited))