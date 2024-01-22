import sys
from collections import deque
input = sys.stdin.readline

deck = deque([])
N = int(input())
for _ in range(N):
    command = input().strip()
    length = len(deck)
    if command.startswith("1"):
        operator, operand = command.split()
        deck.appendleft(operand)
    elif command.startswith("2"):
        operator, operand = command.split()
        deck.append(operand)
    elif command == "3":
        if length == 0:
            print(-1)
        else:
            print(deck.popleft())
    elif command == "4":
        if length == 0:
            print(-1)
        else:
            print(deck.pop())
    elif command == "5":
        print(length)
    elif command == "6":
        if length == 0:
            print(1)
        else:
            print(0)
    elif command == "7":
        if length == 0:
            print(-1)
        else:
            print(deck[0])
    else:
        if length == 0:
            print(-1)
        else:
            print(deck[-1])