import sys
input = sys.stdin.readline

N, M = map(int, input().split())
squares = []
for _ in range(N):
    squares.append(list(input().strip()))
width = 0

max_width = max(N, M)
for i in range(max_width):
    for j in range(N - i):
        for k in range(M - i):
            if (squares[j][k] == squares[j][k+i] 
                and squares[j][k] == squares[j+i][k]
                and squares[j][k] == squares[j+i][k+i]):
                width = max(width, i)

print((width+1)**2)