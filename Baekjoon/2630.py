import sys
input = sys.stdin.readline

def checkFill(area):
    if 0 not in area:
        return "Blue"
    elif 1 not in area:
        return "White"
    return "Mixed"

def divideAndCheck(area, result):
    color = checkFill(area)
    if color == "White":
        result[0] += 1
        return
    elif color == "Blue":
        result[1] += 1
        return
    
    n = int(len(area)**0.5) // 2
    for i in range(2):
        for j in range(2):
            nextArea = []
            for k in range(n):
                nextArea.extend(area[i*len(area)//2+j*n+k*2*n:i*len(area)//2+j*n+k*2*n+n])
            divideAndCheck(nextArea, result)

N = int(input())
colors = []
for _ in range(N):
    colors.extend(list(map(int, input().split())))

answer = [0, 0]
divideAndCheck(colors, answer)
print(answer[0])
print(answer[1])