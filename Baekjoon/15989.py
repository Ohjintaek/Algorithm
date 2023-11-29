import sys
input = sys.stdin.readline

T = int(input())

def oneAndTwo(n):
    return n // 2 + 1

for _ in range(T):
    n = int(input())
    answer = 0
    for i in range(n // 3 + 1):
        answer += oneAndTwo(n - 3*i)
    print(answer)