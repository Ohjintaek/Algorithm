import sys
input = sys.stdin.readline

def divideCheck(N, r, c):
    if N == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3
    
    nr = r // 2**(N-1)
    nc = c // 2**(N-1)
    if nr == 0 and nc == 0:
        return divideCheck(N-1, r - nr*2**(N-1), c - nc*2**(N-1))
    elif nr == 0 and nc == 1:
        return 4**(N-1) + divideCheck(N-1, r - nr*2**(N-1), c - nc*2**(N-1))
    elif nr == 1 and nc == 0:
        return 2*4**(N-1) + divideCheck(N-1, r - nr*2**(N-1), c - nc*2**(N-1))
    else:
        return 3*4**(N-1) + divideCheck(N-1, r - nr*2**(N-1), c - nc*2**(N-1))

N, r, c = map(int, input().split())

print(divideCheck(N, r, c))