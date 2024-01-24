import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)
word_record = dict()
for letter in 'abcdefghijklmnopqrstuvwxyz':
    word_record[letter] = [0]*(n+1)

for i in range(n):
    target = word_record[S[i]]
    word_record[S[i]] = target[:i+1] + [target[i+1] + 1]*(n-i)

q = int(input())
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(word_record[a][r+1] - word_record[a][l])