import sys
input = sys.stdin.readline

N = int(input())
snows = list(map(int, input().split()))
answer = 0
snows.sort(reverse=True)

max_snow = snows[0]
other_snows = sum(snows[1:])
if (max_snow >= other_snows):
    answer = max_snow
else:
    all_snows = max_snow + other_snows
    if (all_snows % 2 == 0):
        answer = all_snows // 2
    else:
        answer = all_snows // 2 + 1 

if (answer > 1440):
    print(-1)
else:
    print(answer)