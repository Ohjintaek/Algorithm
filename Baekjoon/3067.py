import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    bill = int(input())

    coins.sort()
    money = [0 for _ in range(bill+1)]
    for coin in coins:
        for j in range(coin, bill+1):
            money[j] += money[j-coin]
        for j in range(coin, bill+1, coin):
            money[j] += 1

    print(money[bill])