import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = dict()
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

answer = []
for word in words:
    answer.append([word, words[word]])

answer.sort(key = lambda x : x[0])
answer.sort(key = lambda x : len(x[0]), reverse=True)
answer.sort(key = lambda x : x[1], reverse=True)

for word in answer:
    print(word[0])