import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
answer = 0
for number in numbers:
    answer += number**2

print(answer % 10)