import sys
input = sys.stdin.readline

def solution(board, n):
    answer = 0
    if n == 5:
        maxNum = 0
        for i in range(N):
            for j in range(N):
                maxNum = max(maxNum, board[i][j])
        return maxNum
    
    else:
        next = [[0]*N for _ in range(N)]
        for i in range(N):
            index = 0
            present = 0
            canSum = True
            for j in range(N):
                if board[i][j] == 0:
                    continue
                elif board[i][j] == present and canSum:
                    next[i][index-1] *= 2
                    canSum = False
                else:
                    next[i][index] = board[i][j]
                    index += 1
                    present = board[i][j]
                    canSum = True
        answer = max(answer, solution(next, n+1))

        next = [[0]*N for _ in range(N)]
        for i in range(N):
            index = N-1
            present = 0
            canSum = True
            for j in range(N-1, -1, -1):
                if board[i][j] == 0:
                    continue
                elif board[i][j] == present and canSum:
                    next[i][index+1] *= 2
                    canSum = False
                else:
                    next[i][index] = board[i][j]
                    index -= 1
                    present = board[i][j]
                    canSum = True
        answer = max(answer, solution(next, n+1))

        next = [[0]*N for _ in range(N)]
        for i in range(N):
            index = 0
            present = 0
            canSum = True
            for j in range(N):
                if board[j][i] == 0:
                    continue
                elif board[j][i] == present and canSum:
                    next[index-1][i] *= 2
                    canSum = False
                else:
                    next[index][i] = board[j][i]
                    index += 1
                    present = board[j][i]
                    canSum = True
        answer = max(answer, solution(next, n+1))

        next = [[0]*N for _ in range(N)]
        for i in range(N):
            index = N-1
            present = 0
            canSum = True
            for j in range(N-1, -1, -1):
                if board[j][i] == 0:
                    continue
                elif board[j][i] == present and canSum:
                    next[index+1][i] *= 2
                    canSum = False
                else:
                    next[index][i] = board[j][i]
                    index -= 1
                    present = board[j][i]
                    canSum = True
        answer = max(answer, solution(next, n+1))
    
    return answer


N = int(input())
numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

print(solution(numbers, 0))