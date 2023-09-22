import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    peoples = []
    for _ in range(N):
        peoples.append(list(map(int, input().split())))
    peoples.sort(key=lambda x:x[0])

    answer = 1
    temp = peoples[0][1]
    for i in range(1,N):
        if (peoples[i][1] < temp):
            temp = peoples[i][1]
            answer += 1
    
    print(answer)