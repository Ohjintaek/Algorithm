import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def square(n, k):
    if k == 0:
        return 1 % C
    elif k == 1:
        return n % C
    
    next = square(n, k // 2)
    if k % 2 == 0:
        return next * next % C
    else:
        return next * next * n % C

print(square(A, B))