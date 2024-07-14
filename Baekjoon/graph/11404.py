import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

buses = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    buses[i][i] = 0

for _ in range(m):
    fr, to, cost = map(int, input().split())
    buses[fr][to] = min(buses[fr][to], cost)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            buses[j][k] = min(buses[j][k], buses[j][i] + buses[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if buses[i][j] == INF:
            print(0, end = ' ')
        else:
            print(buses[i][j], end = ' ')