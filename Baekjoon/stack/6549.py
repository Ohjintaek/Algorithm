import sys
input = sys.stdin.readline

while True:
    _input = list(map(int, input().split()))
    N, heights = _input[0], _input[1:]
    if N == 0:
        break

    stack = []
    result = 0
    for i in range(N):
        index = i
        while stack and stack[-1][1] > heights[i]:
            index, height = stack.pop()
            result = max(result, (i - index)*height)
        stack.append([index, heights[i]])
    
    while stack:
        index, height = stack.pop()
        result = max(result, (N-index)*height)
    
    print(result)