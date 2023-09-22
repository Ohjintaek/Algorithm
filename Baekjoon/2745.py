import sys
input = sys.stdin.readline

N, B = input().split()

# A = 65, Z = 90
numbers = [str(i) for i in range(10)]
numbers.extend([chr(i) for i in range(65, 91)])
answer = 0

for i in range(len(N)):
    index = len(N) - 1 - i
    answer += numbers.index(N[index]) * (int(B)**i)

print(answer)