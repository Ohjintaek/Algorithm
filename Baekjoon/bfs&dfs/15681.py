import sys
input = sys.stdin.readline

def makeDP(start):
    visited[start] = True
    if childNum[start] == 0:
        result = 1
        for child in tree[start]:
            if not visited[child]:
                result += makeDP(child)
        childNum[start] = result
    return childNum[start]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _  in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False]*(N+1)
childNum = [0]*(N+1)
makeDP(R)

for i in range(Q):
    u = int(input())
    print(childNum[u])