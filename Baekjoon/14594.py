import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
room = [1 for i in range(N-1)]

for _ in range(M):
    x, y = map(int, input().split())
    room[x-1:y-1] = [0 for i in range(y-x)]

print(sum(room)+1)