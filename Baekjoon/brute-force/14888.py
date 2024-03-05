import sys
import itertools
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_answer = 1000000000
max_answer = -1000000000

candidates = itertools.permutations(''.join([str(i+1)*operators[i] for i in range(4)]))
for candidate in candidates:
    number = numbers[0]
    for i in range(N-1):
        if candidate[i] == '1':
            number += numbers[i+1]
        elif candidate[i] == '2':
            number -= numbers[i+1]
        elif candidate[i] == '3':
            number *= numbers[i+1]
        else:
            if number < 0:
                number = -(abs(number)//numbers[i+1])
            else:
                number //= numbers[i+1]
    min_answer = min(min_answer, number)
    max_answer = max(max_answer, number)

print(max_answer)
print(min_answer)