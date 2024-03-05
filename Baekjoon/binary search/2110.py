import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

left = 0
right = 1000000000

while left <= right:
    mid = (left + right)//2
    cnt = 1
    position = houses[0]
    for i in range(1,N):
        if houses[i] - position >= mid:
            cnt += 1
            position = houses[i]
    if cnt >= C:
        left = mid + 1
    else:
        right = mid - 1

print(right)