import sys
input = sys.stdin.readline

def roundUp(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(input())
suggestions = []
for _ in range(n):
    suggestions.append(int(input()))

suggestions.sort()
cutNum = roundUp(n*0.15)
targetSuggestions = suggestions[cutNum:n-cutNum]

if n == 0:
    print(0)
else:
    answer = roundUp(sum(targetSuggestions)/(n-2*cutNum))
    print(answer)