import sys
input = sys.stdin.readline

T = int(input())
answer = [[] for i in range(64)]
answer[0].extend([i+1 for i in range(10)])
for i in range(1, 64):
    temp = []
    for j in range(10):
        temp.append(sum(answer[i-1][:j+1]))
    answer[i].extend(temp)

for _ in range(T):
    n = int(input())
    print(answer[n-1][9])