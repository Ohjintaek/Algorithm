import sys
import math
input = sys.stdin.readline

N = int(input())
sizes =list(map(int, input().split()))
T, P = map(int, input().split())

Tmass = 0
for size in sizes:
    Tmass += math.ceil(size/T)

Pmass, Peach = N // P, N % P

print(Tmass)
print(Pmass, Peach)