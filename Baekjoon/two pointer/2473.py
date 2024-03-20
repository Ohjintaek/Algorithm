import sys
input = sys.stdin.readline

N = int(input())
fluids = list(map(int, input().split()))
fluids.sort()

tmp = 3000000000
flag = False
for i in range(N):
    if flag:
        break

    delta = fluids[i]
    tmpFluids = fluids[i+1:]
    
    left, right = 0, N - (i+2)
    while left < right:
        if abs(tmpFluids[left] + tmpFluids[right] + delta) < tmp:
            tmp = abs(tmpFluids[left] + tmpFluids[right] + delta)
            ans = [delta, tmpFluids[left], tmpFluids[right]]

        if tmpFluids[left] + tmpFluids[right] + delta < 0:
            left += 1
        elif tmpFluids[left] + tmpFluids[right] + delta > 0:
            right -= 1
        else:
            ans = [delta, tmpFluids[left], tmpFluids[right]]
            flag = True
            break

print(*sorted(ans))