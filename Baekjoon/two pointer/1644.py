import sys
input = sys.stdin.readline

def makePrimeList(n):
    isPrime = [False, False] + [True]*(n-1)
    _list = []

    for i in range(2, n+1):
        if isPrime[i]:
            _list.append(i)
            for j in range(2*i, N+1, i):
                isPrime[j] = False
    
    return _list

N = int(input())
primes = makePrimeList(N)

prefixPrime = [0]
for prime in primes:
    prefixPrime.append(prefixPrime[-1] + prime)

cnt = 0
left, right = 0, 1
while right < len(prefixPrime):
    tmp = prefixPrime[right] - prefixPrime[left]
    if tmp > N:
        left += 1
    elif tmp < N:
        right += 1
    else:
        cnt += 1
        right += 1

print(cnt)