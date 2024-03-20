import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
left, right = 0, N-1
ans = [liquids[left], liquids[right]]
tempSum = abs(sum(ans))

while left < right:
    if abs(liquids[left] + liquids[right]) < tempSum:
        tempSum = abs(liquids[left] + liquids[right])
        ans = [liquids[left], liquids[right]]
    if tempSum == 0:
        break

    if abs(liquids[left + 1] + liquids[right]) <= abs(liquids[left] + liquids[right-1]):
        left += 1
    else:
        right -= 1

print(*sorted(ans))