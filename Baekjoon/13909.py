import sys
input = sys.stdin.readline

N = int(input())
answer = 1
while (answer*answer <= N):
    answer += 1
print(answer - 1)