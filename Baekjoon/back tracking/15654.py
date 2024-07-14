import sys
input = sys.stdin.readline

def solution(numbers, _list, length):
    if length == M:
        print(*_list)
    
    else:
        for i in range(len(numbers)):
            solution(numbers[:i] + numbers[i+1:], _list + [numbers[i]], length+1)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
solution(numbers, [], 0)