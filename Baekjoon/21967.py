import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
elem_index = [-1 for _ in range(11)]
answer = 1
start = -1

for i in range(N):
    elem_index[numbers[i]] = i
    for j in range(1,11):
        if (abs(j - numbers[i])) > 2:
            start = max(start, elem_index[j])
    answer = max(answer, i-start)

print(answer)


import sys

input = sys.stdin.read


def sol21967():
    n, *nums = map(int, input().split())
    dp = [0] * (n + 1)

    mi = ma = 0
    cnt = 0
    i = 0
    while i < n:
        mi = i if nums[i] <= nums[mi] else mi
        ma = i if nums[i] >= nums[ma] else ma
        if nums[ma] - nums[mi] > 2:
            i = min(mi, ma) + 1
            mi = ma = i
            dp[i - 1] = cnt
            cnt = 0
        else:
            i += 1
            cnt += 1
    print(max(*dp, cnt))


if __name__ == '__main__':
    sol21967()