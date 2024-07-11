import sys
input = sys.stdin.readline

n = int(input())
dp = [5]*(n+1)

squarelst = []
for i in range(1, int(n**0.5) + 1):
    squarelst.append(i**2)
    dp[i**2] = 1

for i in range(2, 5):
    toVisit = []
    for j in range(1, n):
        if dp[j] == i-1:
            toVisit.append(j)
    
    for j in range(len(toVisit)):
        for k in range(len(squarelst)):
            target = toVisit[j] + squarelst[k]
            if target > n:
                break

            if dp[target] == 5:
                dp[target] = i
            
print(dp[n])