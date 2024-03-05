import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer_numbers = set(map(str, input().split()))

cnt = 0

for i in range(10**n):
    number = str(i)
    comparable = set(str(i))
    if i < 10**(n-1):
        comparable.add('0')
    if answer_numbers.issubset(comparable):
        cnt += 1

print(cnt)