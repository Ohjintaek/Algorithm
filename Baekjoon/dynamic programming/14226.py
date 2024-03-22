import sys
input = sys.stdin.readline

S = int(input())

dp = [[0 for _ in range(S+1)] for _ in range(S+1)]
visited = [[False for _ in range(S+1)] for _ in range(S+1)]

def bfs(start):
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = True

    flag = False
    while queue:
        tmp = []
        for node in queue:
            pos, paste = node[0], node[1]
            value = dp[pos][paste]
            
            if pos >= 1 and not visited[pos-1][paste]:
                tmp.append((pos-1, paste))
                dp[pos-1][paste] = value + 1
                visited[pos-1][paste] = True
            
            if not visited[pos][pos]:
                tmp.append((pos, pos))
                dp[pos][pos] = value + 1
                visited[pos][pos] = True
            
            if paste > 0 and pos + paste <= S and not visited[pos + paste][paste]:
                tmp.append((pos + paste, paste))
                dp[pos + paste][paste] = value + 1
                visited[pos + paste][paste] = True
            
            if pos-1 == S or pos + paste == S:
                flag = True
                break

        if flag:
            break
        queue = tmp

bfs((1, 0))
for num in dp[S]:
    if num != 0:
        print(num)