import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []
for i in range(n):
    for j in range(n):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])

AB.sort()
CD.sort()

answer = 0
left, right = 0, n*n-1
while left < n*n and right >= 0:
    ABnum = 1
    while left + 1 < n*n and AB[left] == AB[left+1]:
        left += 1
        ABnum += 1
    
    CDnum = 1
    while right - 1 >= 0 and CD[right] == CD[right-1]:
        right -= 1
        CDnum += 1
    
    if AB[left] + CD[right] == 0:
        answer += ABnum*CDnum
        left += 1
        right -= 1
    elif AB[left] + CD[right] < 0:
        left += 1
        right += (CDnum-1)
    else:
        right -= 1
        left -= (ABnum-1)

print(answer)