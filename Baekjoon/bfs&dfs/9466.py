import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    selection = list(map(int, input().split()))

    remain = set([i+1 for i in range(N)])
    visited = [False]*(N+1)
    answer = 0
    for i in range(1, N+1):
        if visited[i]:
            continue

        temp = {i: 0}
        visited[i] = True
        person = i
        next = selection[person-1]
        while next != i:
            if next in temp:
                answer += temp[next]
                break

            if visited[next]:
                answer += (temp[person] + 1)
                break

            temp[next] = temp[person] + 1
            visited[next] = True
            person = next
            next = selection[next-1]
            
    print(answer)