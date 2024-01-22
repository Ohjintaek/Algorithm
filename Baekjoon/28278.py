import sys
from collections import deque
input = sys.stdin.readline

stack = deque([])
N = int(input())
for _ in range(N):
    command = input().strip()
    if command.startswith("1"):
        operator, operand = command.split()
        stack.append(operand)
    elif command == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "3":
        print(len(stack))
    elif command == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])