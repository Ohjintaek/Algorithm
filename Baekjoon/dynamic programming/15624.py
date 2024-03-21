import sys
input = sys.stdin.readline

n = int(input())

fibonacci = [0,1]
for _ in range(n-1):
    fibonacci.append((fibonacci[-2] + fibonacci[-1]) % 1000000007)

print(fibonacci[-1])