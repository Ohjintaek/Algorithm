import sys
input = sys.stdin.readline

N = int(input())
numbers = []
cnt = 0
number = 666
devil = '666'
while True:
    if cnt > 10000:
        break
    if devil in str(number):
        numbers.append(number)
        cnt += 1
    number += 1

print(numbers[N-1])