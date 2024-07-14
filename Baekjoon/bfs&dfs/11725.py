import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _  in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = []
visited = [False]*(N+1)
queue.append(1)
visited[1] = True

while queue:
    temp = []
    for node in queue:
        for child in tree[node]:
            if not visited[child]:
                visited[child] = node
                temp.append(child)
    queue = temp

for i in range(2, N+1):
    print(visited[i])