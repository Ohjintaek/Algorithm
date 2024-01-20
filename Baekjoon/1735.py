import sys
input = sys.stdin.readline

def Euclidean(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())

gcd = Euclidean(B, D)
parent = B*D//gcd
child = A*D//gcd + C*B//gcd
new_gcd = Euclidean(parent, child)
print(child//new_gcd, parent//new_gcd)