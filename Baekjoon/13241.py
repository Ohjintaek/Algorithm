import sys
input = sys.stdin.readline

def Euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
gcd = Euclidean(A, B)
print(A*B//gcd)