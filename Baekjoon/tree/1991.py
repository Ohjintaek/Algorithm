import sys
input = sys.stdin.readline

N = int(input())
tree = dict()
for _ in range(N):
    value, left, right = map(str, input().split())
    tree[value] = [left, right]

def preOrder(node):
    if node not in tree:
        return
    print(node, end='')
    preOrder(tree[node][0])
    preOrder(tree[node][1])

def inOrder(node):
    if node not in tree:
        return
    inOrder(tree[node][0])
    print(node, end='')
    inOrder(tree[node][1])

def postOrder(node):
    if node not in tree:
        return
    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(node, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')