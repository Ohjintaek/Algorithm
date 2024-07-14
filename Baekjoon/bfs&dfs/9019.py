import sys
input = sys.stdin.readline

def bfs(A, B):
    queue = []
    visit = [False]*10000
    queue.append([A, ''])
    visit[A] = True

    end = False
    while queue:
        if end:
            break
        
        temp = []
        for node in queue:
            register, command = node[0], node[1]
            if register == B:
                end = True
                result = command
                break
            
            # D 연산
            number = register*2 % 10000
            if not visit[number]:
                visit[number] = True
                temp.append([number, command+'D'])

            # S 연산
            number = register - 1
            if number < 0:
                number = 9999
            if not visit[number]:
                visit[number] = True
                temp.append([number, command+'S'])

            # L 연산
            number = (register%1000)*10 + register//1000
            if not visit[number]:
                visit[number] = True
                temp.append([number, command+'L'])

            # R 연산
            number = register//10 + (register%10)*1000
            if not visit[number]:
                visit[number] = True
                temp.append([number, command+'R'])

        queue = temp
    return result

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))