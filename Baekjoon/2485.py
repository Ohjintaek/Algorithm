import sys
input = sys.stdin.readline

def Euclidean(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

N = int(input())
numbers = [int(input())]
intervals = set()
for _ in range(N-1):
    number = int(input())
    intervals.add(number - numbers[-1])
    numbers.append(number)

gcd = intervals.pop()
for interval in intervals:
    gcd = Euclidean(gcd, interval)

temp = (numbers[-1] - numbers[0]) // gcd
answer = temp + 1 - N
print(answer)