import sys
input = sys.stdin.readline

def matrixMul(A, B):
    N = len(A)
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            value = 0
            for k in range(N):
                value += A[i][k]*B[k][j]
            row.append(value % 1000)
        matrix.append(row)
    
    return matrix

def function(A, n):
    if n == 1:
        return A
    
    if n % 2 == 0:
        return function(matrixMul(A, A), n//2)
    else:
        return matrixMul(function(matrixMul(A, A), n//2), A)

N, B = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(N):
    for j in range(N):
        matrix[i][j] %= 1000

for row in function(matrix, B):
    print(*row)