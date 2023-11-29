import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = set()

for _ in range(N):
    keywords.add(input().strip())
answer = len(keywords)

for _ in range(M):
    writings = list(input().strip().split(','))
    for word in writings:
        if word in keywords:
            keywords.remove(word)
            answer -= 1
    print(answer)