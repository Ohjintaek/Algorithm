import sys
input = sys.stdin.readline

def solution(string, n, index):
    if n == M:
        print(string.lstrip())
    else:
        for i in range(index, len(sortedNumbers)):
            solution(string + ' ' + str(sortedNumbers[i]), n+1, i)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sortedNumbers = sorted(set(numbers))
solution("", 0, 0)