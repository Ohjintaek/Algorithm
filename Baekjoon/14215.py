import sys
input = sys.stdin.readline

length = list(map(int, input().split()))
length.sort()

if (length[0] + length[1] <= length[2]):
    print(2*(length[0] + length[1]) - 1)
else:
    print(length[0] + length[1] + length[2]) 