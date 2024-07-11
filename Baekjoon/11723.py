import sys
input = sys.stdin.readline

M = int(input())
S = [0]*20
for _ in range(M):
    operation = list(input().split())
    
    if operation[0] == 'add':
        target = int(operation[1])
        S[target-1] = 1
    
    elif operation[0] == 'remove':
        target = int(operation[1])
        S[target-1] = 0

    elif operation[0] == 'check':
        target = int(operation[1])
        if S[target-1]:
            print(1)
        else:
            print(0)

    elif operation[0] == 'toggle':
        target = int(operation[1])
        if S[target-1]:
            S[target-1] = 0
        else:
            S[target-1] = 1


    elif operation[0] == 'all':
        S = [1]*20

    else:
        S = [0]*20