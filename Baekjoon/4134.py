import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0 or n == 1:
        print(2)
        continue
    answer = n
    flag = False
    while(True):
        for i in range(2, int((answer)**0.5) + 1):
            if answer % i == 0:
                flag = True
                break
        if flag:
            answer += 1
            flag = False
            continue
        print(answer)
        break