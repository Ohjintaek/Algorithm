import sys
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    operation = list(input().split())

    if operation[0] == 'push':
        target = int(operation[1])
        queue.append(target)
    
    elif operation[0] == 'pop':
        if queue:
            print(queue[0])
            queue = queue[1:]
        else:
            print(-1)
    
    elif operation[0] == 'size':
        print(len(queue))

    elif operation[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif operation[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)