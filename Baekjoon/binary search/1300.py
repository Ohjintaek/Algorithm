import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

left = 1
right = N*N

while left <= right:
    mid = (left+right) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, mid//i)
    
    if cnt < k:
        left = mid + 1
    else:
        right = mid - 1

print(left)