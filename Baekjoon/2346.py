import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
temp_numbers = list(map(int, input().split()))
numbers = deque([])
for i in range(N):
    numbers.append([temp_numbers[i], i+1])
order = []

length = N
while (length > 1):
    out = numbers.popleft()
    length -= 1
    counter = out[0]
    order.append(out[1])
    if counter > 0:
        out = (counter - 1) % length
        for _ in range(out):
            numbers.append(numbers.popleft())
    else:
        out = (-counter) % length
        for _ in range(out):
            numbers.appendleft(numbers.pop())
order.append(numbers.pop()[1])
print(*order)