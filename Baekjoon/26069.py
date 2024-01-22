import sys
input = sys.stdin.readline

N = int(input())
dancePeople = set()
dancePeople.add("ChongChong")

for _ in range(N):
    A, B = input().split()
    if A in dancePeople:
        dancePeople.add(B)
    elif B in dancePeople:
        dancePeople.add(A)

print(len(dancePeople))