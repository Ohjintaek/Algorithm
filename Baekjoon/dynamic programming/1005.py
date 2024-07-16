import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(number):
    if dp[number] >= 0:
        return dp[number]
    else:
        result = 0
        for prev in orders[number]:
            result = max(result, solution(prev))
        dp[number] = costs[number-1] + result
        return dp[number]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    costs = list(map(int, input().split()))

    orders = [[] for _ in range(N+1)]
    start = set([i+1 for i in range(N)])
    for _ in range(K):
        fr, to = map(int, input().split())
        orders[to].append(fr)
        start.discard(to)
    W = int(input())

    dp = [-1]*(N+1)
    dp[0] = 0

    print(solution(W))