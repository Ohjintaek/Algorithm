import sys
input = sys.stdin.readline
mod = 1000000007

N, K = map(int, input().split())
K = min(N-K, K)

def square(n, k):
    if k == 0:
        return 1 % mod
    elif k == 1:
        return n % mod
    
    next = square(n, k // 2)
    if k % 2 == 0:
        return next * next % mod
    else:
        return next * next * n % mod

def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i+1
        result %= mod
    return result

result = ((factorial(N) % mod) * square((factorial(N-K)*factorial(K)), mod - 2) % mod) % mod
print(result)