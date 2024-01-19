import sys
input = sys.stdin.readline

while(True):
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        break

    arr = [a, b, c]
    arr.sort(reverse = True)
    if (arr[0] >= arr[1] + arr[2]):
        print("Invalid")
        continue
    set_arr = set(arr)

    if (len(set_arr) == 1):
        print("Equilateral")
    elif (len(set_arr) == 2):
        print("Isosceles")
    else:
        print("Scalene")