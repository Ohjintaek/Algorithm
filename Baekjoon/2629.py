import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
T = int(input())
marbles = list(map(int, input().split()))

can = set()

for weight in weights:
    temp = set()
    for number in can:
        temp.add(number - weight)
        temp.add(number + weight)
    can.add(weight)
    can.add(-weight)
    can = can.union(temp)

print(can)
for marble in marbles:
    if marble in can:
        print("Y", end = ' ')
    else:
        print("N", end = ' ')