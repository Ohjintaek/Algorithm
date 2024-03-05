import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

left = 1
right = max(lines)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)