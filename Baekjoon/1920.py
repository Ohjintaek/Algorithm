import sys
input = sys.stdin.readline

N = int(input())
Nnumbers = list(map(int, input().split()))
M = int(input())
Mnumbers = list(map(int, input().split()))

Nnumbers.sort()
for i in range(M):
    target = Mnumbers[i]
    left = 0
    right = N-1
    while(left <= right):
        mid = (left + right) // 2
        if target < Nnumbers[mid]:
            right = mid - 1
        elif target > Nnumbers[mid]:
            left = mid + 1
        else:
            break
    if left <= right:
        print(1)
    else:
        print(0)