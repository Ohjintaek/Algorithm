import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floors = [[i for i in range(n+1)]]
    for i in range(1,k+1):
        floors.append([0])
        for j in range(1,n+1):
            floors[i].append(floors[i][j-1] + floors[i-1][j])
    print(floors[k][n])