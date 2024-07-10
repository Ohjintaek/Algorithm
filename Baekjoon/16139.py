import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)

alpha_dict = dict()
for letter in 'abcdefghijklmnopqrstuvwxyz':
    alpha_dict[letter] = 0
word_record = {0 : alpha_dict}

for i in range(n):
    word_record[i+1] = word_record[i].copy()
    word_record[i+1][S[i]] += 1

q = int(input())
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(word_record[r+1][a] - word_record[l][a])