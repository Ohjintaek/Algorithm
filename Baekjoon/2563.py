import sys
input = sys.stdin.readline

result = [[0]*100 for _ in range(100)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y + 10):
            result[i][j] = 1

answer = 0
for elem in result:
    answer += elem.count(1)

print(answer)