import sys
input = sys.stdin.readline

word = input().strip()
result = word == word[::-1]

if (result):
    print(1)
else:
    print(0)