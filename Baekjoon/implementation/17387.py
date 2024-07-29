import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def funcA(x):
    return (y2-y1)/(x2-x1)*x + y1 - (y2-y1)/(x2-x1)*x1

def funcB(x):
    return (y4-y3)/(x4-x3)*x + y3 - (y4-y3)/(x4-x3)*x3

if x1 > x2:
    x1, y1, x2, y2 = x2, y2, x1, y1

if x3 > x4:
    x3, y3, x4, y4 = x4, y4, x3, y3

startX, endX = max(x1, x3), min(x2, x4)
if endX < startX:
    print(0)
else:
    if (x2 - x1 == 0) and (x4 - x3 == 0):
        if (min(y3, y4) <= y1 <= max(y3, y4)) | (min(y3, y4) <= y2 <= max(y3, y4)):
            print(1)
        else:
            print(0)
    elif x2 - x1 == 0:
        if min(y1, y2) <= funcB(x1) <= max(y1, y2):
            print(1)
        else:
            print(0)
    elif x4 - x3 == 0:
        if min(y3, y4) <= funcA(x3) <= max(y3, y4):
            print(1)
        else:
            print(0)    
    else:
        flag = (funcA(startX) > funcB(startX)) ^ (funcA(endX) > funcB(endX)) | (round(funcA(startX), 9) == round(funcB(startX), 9)) | (round(funcA(endX), 9) == round(funcB(endX), 9))
        if flag:
            print(1)
        else:
            print(0)