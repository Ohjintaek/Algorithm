import sys
input = sys.stdin.readline

N = int(input())
answer = 1
for i in range(N):
    answer *= i+1
print(answer)