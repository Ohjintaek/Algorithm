import sys
input = sys.stdin.readline

arr = []
for _ in range(3):
    arr.append(int(input()))

set_arr = set(arr)
if (sum(arr) != 180):
    print("Error")
else:
    if (len(set_arr) == 1):
        print("Equilateral")
    elif (len(set_arr) == 2):
        print("Isosceles")
    else:
        print("Scalene")