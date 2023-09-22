import sys
input = sys.stdin.readline

while(True):
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        break

    arr = [a, b, c]
    set_arr = set(arr)

    if (len(set_arr) == 1):
        print("Equilateral")
    elif (len(set_arr) == 2):
        if (set_arr.remove(0)):
            print("Invalid")
        print("Isosceles")
    else:
        arr.sort(revers = True)
        if (arr[0] >= )