import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    flights = [[] for _ in range(N+1)]
    for _ in range(M):
        fr, to = map(int, input().split())
        flights[fr].append(to)
        flights[to].append(fr)
    
    print(N-1) 