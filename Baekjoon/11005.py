import sys
input = sys.stdin.readline

N, B = map(int, input().split())

numbers = [str(i) for i in range(10)]
numbers.extend([chr(i) for i in range(65, 91)])

answer = []
div = N

while(True):
    if (div < B):
        answer.insert(0, numbers[div])
        break
    answer.insert(0, numbers[div % B])
    div = div // B

print(*answer, sep = "")