import sys
import math
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

points.append(points[0])

answer = 0
for i in range(N):
    answer += points[i][0]*points[i+1][1]
    answer -= points[i][1]*points[i+1][0]

print(round(abs(answer/2), 1))