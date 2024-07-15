import sys
input = sys.stdin.readline

N = int(input())
fluids = list(map(int, input().split()))

left, right = 0, N-1
value = abs(fluids[left] + fluids[right])
answer = [fluids[left], fluids[right]]

while left < right:
    if abs(fluids[left] + fluids[right]) < value:
        value = abs(fluids[left] + fluids[right])
        answer = [fluids[left], fluids[right]]
    
    if abs(fluids[left+1] + fluids[right]) <= abs(fluids[left] + fluids[right-1]):
        left += 1
    else:
        right -= 1

print(*answer)