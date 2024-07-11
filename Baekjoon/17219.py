import sys
input = sys.stdin.readline

N, M = map(int, input().split())
passwordMap = dict()
for _ in range(N):
    site, password = input().split()
    passwordMap[site] = password

for _ in range(M):
    print(passwordMap[input().strip()])