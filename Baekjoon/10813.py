import sys

input = sys.stdin.readline
N, M = map(int, input().split())
number = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = number[i-1]
    number[i-1] = number[j-1]
    number[j-1] = temp

print(*number)