import sys
input = sys.stdin.readline

MAX = 1000000
primes = [True for _ in range(MAX)]
primes[2] = True
primes[3] = True

for i in range(2, 1000):
    if primes[i]:
        for j in range(i*i, MAX, i):
            primes[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    answer = 0
    for i in range(2, N//2 + 1):
        if primes[i] and primes[N-i]:
            answer += 1
    print(answer)