import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

scores = dict(zip(numbers, [0]*N))
sortedNumbers = sorted(numbers)
for number in sortedNumbers:
    for i in range(number*2, sortedNumbers[-1]+1, number):
        if i in scores:
            scores[number] += 1
            scores[i] -= 1

for i in range(N):
    print(scores[numbers[i]], end = ' ')