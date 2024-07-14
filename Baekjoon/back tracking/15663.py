import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
_set = set()

def solution(numbers, _list, length):
    if length == M:
        print(*_list)
    
    else:
        for i in range(len(numbers)):
            target = _list + [numbers[i]]
            if '.'.join(map(str, target)) not in _set:
                _set.add('.'.join(map(str, target)))
                solution(numbers[:i] + numbers[i+1:], target, length+1)

solution(numbers, [], 0)