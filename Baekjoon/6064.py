import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    # Ma - Nb = x - y가 되는 a, b를 찾는다
    # 순서는 해가 있다면 M*a+x 또는 N*B+y
    a, b = 0, 0
    target = y - x
    flag = False
    while a < N or b < M:
        if M*a - N*b > target:
            b += 1
        elif M*a - N*b < target:
            a += 1
        else:
            flag = True
            break
    
    if flag:
        print(M*a + x)
    else:
        print(-1)