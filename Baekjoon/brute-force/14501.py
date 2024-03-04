import sys
input = sys.stdin.readline

N = int(input())

counsellings = []
for _ in range(N):
    counsellings.append(list(map(int, input(). split())))

answer = 0

def recursive(day, remain, money):
    global answer
    remain -= 1
    if day == N:
        if remain <= 0:
            answer = max(answer, money)
        return
    if remain <= 0:
        recursive(day + 1, counsellings[day][0], money + counsellings[day][1])
    recursive(day + 1, remain, money)

recursive(0, 0, 0)
print(answer)