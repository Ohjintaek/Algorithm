import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C = int(input())
    answer = []
    coins = [25, 10, 5, 1]
    for coin in coins:
        answer.append(C // coin)
        C = C % coin
    print(*answer)
