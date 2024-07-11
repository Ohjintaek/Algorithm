import sys
input = sys.stdin.readline

while True:
    number = input().strip()
    if number == '0':
        break

    reverseNumber = number[::-1]
    if number == reverseNumber:
        print('yes')
    else:
        print('no')