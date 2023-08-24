import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    numbers[i-1:j] = list(reversed(numbers[i-1:j]))

print(*numbers)