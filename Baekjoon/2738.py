import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for row in range(N):
    for col in range(M):
        print(A[row][col]+B[row][col], end=" ")
    print()