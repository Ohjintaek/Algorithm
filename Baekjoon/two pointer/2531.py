import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

sushi.extend(sushi)

ans = 0
for i in range(N):
    eat = set(sushi[i:i+k])
    if c in eat:
        tmp = len(eat)
    else:
        tmp = len(eat) + 1
    ans = max(ans, tmp)

print(ans)
