import sys
input = sys.stdin.readline

N = int(input())
plans = []

for _ in range(N):
    plans.append(list(map(int, input().split())))
plans.sort(key = lambda x : x[0])

answer = 0
profit = 0
for i in range(len(plans)):
    price = plans[i][0]
    temp_profit = 0
    for plan in plans:
        if (plan[0] >= price) and (price > plan[1]):
            temp_profit += (price - plan[1])
    if (temp_profit > profit):
        answer = price
        profit = temp_profit

print(answer)