import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
standard = '12345678'

isAsc = True
isDesc = True
for i in range(8):
    if numbers[i] != int(standard[i]):
        isAsc = False
    if numbers[i] != int(standard[7-i]):
        isDesc = False

if isAsc:
    print('ascending')
elif isDesc:
    print('descending')
else:
    print('mixed')