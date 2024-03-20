import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

cnt = 0
ans = N + 1
left = 0
for right in range(N):
    if dolls[right] == 1:
        cnt += 1
    
    while left <= right:
        if dolls[left] == 2:
            left += 1
        elif cnt == K + 1 and dolls[left] == 1:
            cnt -= 1
            left += 1
        else:
            break
    
    if cnt == K:
        ans = min(ans, right - left + 1)

if ans == N + 1:
    print(-1)
else:
    print(ans)