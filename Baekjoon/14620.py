import sys
input = sys.stdin.readline

def calc_price(i, j, prices):
    return prices[i][j] + prices[i-1][j] + prices[i+1][j] + prices[i][j-1] + prices[i][j+1]

def isAdjusted(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) <= 2

def dfs(visited, total):
    global answer
    if (len(visited) == 3):
        answer = min(answer, total)
        return

    row = 1
    if visited:
        row = visited[-1][0]

    for i in range(row, N-1):
        for j in range(1, N-1):
            flag = False
            for visit in visited:
                if isAdjusted(visit, [i,j]):
                    flag = True
                    break
            if flag:
                continue

            next_visited = visited + [[i,j]]
            next_total = total + calc_price(i, j, prices)
            if next_total >= answer:
                continue
            dfs(next_visited, next_total)

N = int(input())

prices = []
for _ in range(N):
    prices.append(list(map(int, input().split())))

answer = 200*15
dfs([], 0)

print(answer)