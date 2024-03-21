import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000007

fibonacci = [0,1]
for _ in range(n-1):
    # 모듈로 연산
    fibonacci.append((fibonacci[-2] % mod + fibonacci[-1] % mod) % mod)

if n == 0:
    print(0)
else:
    print(fibonacci[-1])