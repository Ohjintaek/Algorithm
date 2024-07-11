import sys
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

answer = 0
newFruit = fruits[:1]
start, right = 0, 1

while len(newFruit) < 2 and right < N:
    if fruits[right] not in newFruit:
        newFruit.append(fruits[right])
        break
    right += 1

next = right
while right < N:
    if fruits[right] not in newFruit:
        answer = max(answer, right - start)
        newFruit.remove(fruits[next-1])
        newFruit.append(fruits[right])
        start = next
        next = right
    else:
        if fruits[right] != fruits[next]:
            next = right
    right += 1
    
answer = max(answer, right-start)
print(answer)