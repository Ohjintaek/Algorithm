import sys
input = sys.stdin.readline

N, K = map(int, input().split())
divisors = []
answer = 0

for i in range(1, N + 1):
    if (N % i == 0):
        divisors.append(i)
        if(len(divisors) == K):
            answer = i
            break

print(answer)
