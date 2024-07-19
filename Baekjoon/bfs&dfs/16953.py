import sys
input = sys.stdin.readline

def dfs(number, n):
    if number == B:
        return (True, n+1)
    if number > B:
        return (False, -1)
    
    result = dfs(number*10+1, n+1)
    if result[0]:
        return result

    result = dfs(number*2, n+1)
    if result[0]:
        return result

    return (False, -1)    


A, B = map(int, input().split())
print(dfs(A, 0)[1])