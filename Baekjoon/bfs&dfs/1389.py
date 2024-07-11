import sys
input = sys.stdin.readline

def bfs(start, n):
    visit = [-1]*n
    queue = []
    queue.append(start)
    visit[start-1] = 0

    distance = 1
    while queue:
        temp = set()
        for node in queue:
            for friend in friendships[node]:
                if visit[friend-1] == -1:
                    visit[friend-1] = distance
                    temp.add(friend)
        queue = list(temp)
        distance += 1
    
    return visit

N, M = map(int, input().split())
friendships = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    friendships[A].add(B)
    friendships[B].add(A)

answerValue = 100000000
answer = 1
for i in range(1, N+1):
    friendWeb = bfs(i, N)
    baconNum = sum(friendWeb)
    if baconNum < answerValue:
        answerValue = baconNum
        answer = i

print(answer)