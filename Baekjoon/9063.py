import sys
input = sys.stdin.readline

N = int(input())
minx, miny = 10000, 10000
maxx, maxy = -10000, -10000
for _ in range(N):
    x, y = map(int, input().split())
    minx = min(x, minx)
    miny = min(y, miny)
    maxx = max(x, maxx)
    maxy = max(y, maxy)

print((maxx-minx)*(maxy-miny))