import sys
input = sys.stdin.readline

def makePrimeList(n):
    _list = [2]
    for i in range(3, n+1):
        flag = True
        for num in _list:
            if num > int(i**0.5):
                break
            if i % num == 0:
                flag = False
                break
        if flag:
            _list.append(i)
    
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