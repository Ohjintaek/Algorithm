import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
weights.sort()

max_value = 0
for i in range(N):
    if weights[i] > max_value + 1:
        break
    max_value += weights[i]

print(max_value + 1)