import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

def getPreOrder(postIndex, inIndex, length):
    if length == 0:
        return
    
    value = postOrder[postIndex + length - 1]
    print(value, end=' ')
    if length == 1:
        return
    
    left = 0
    for i in range(length):
        if value == inOrder[inIndex + i]:
            left = i
            break
    
    getPreOrder(postIndex, inIndex, left)
    getPreOrder(postIndex + left, inIndex + left + 1, length - left - 1)

getPreOrder(0, 0, n)