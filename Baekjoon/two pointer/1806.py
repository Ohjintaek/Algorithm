import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

prefixSum = [0]
for num in numbers:
    prefixSum.append(prefixSum[-1] + num)

left, right = 1, 1

ans = N+1
while right < N+1:
    if prefixSum[right] - prefixSum[left-1] >= S:
        ans = min(ans, right - left + 1)
        left += 1
    else:
        right += 1

if ans == N+1:
    print(0)
else:
    print(ans)