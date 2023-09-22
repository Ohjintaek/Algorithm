import sys
input = sys.stdin.readline

words = []
max_word_length = 1
answer = ""

for _ in range(5):
    word = input().strip()
    if len(word) > max_word_length:
        max_word_length = len(word)
    words.append(word)

for i in range(max_word_length):
    for j in range(5):
        if len(words[j]) > i:
            answer += words[j][i]
            
print(answer)
