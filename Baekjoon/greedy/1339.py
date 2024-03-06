import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())

words.sort(key = lambda x : len(x), reverse=True)
max_length = len(words[0])
anal_dict = dict()

for i in range(max_length):
    for word in words:
        length = len(word)
        if length >= max_length - i:
            if word[length - max_length + i] not in anal_dict:
                anal_dict[word[length - max_length + i]] = 10**(max_length - 1 - i)
            else:
                anal_dict[word[length - max_length + i]] += 10**(max_length - 1 - i)

temp_list = sorted(anal_dict.items(), key = lambda x : x[1], reverse=True)

answer_dict = dict()
index = 9
for temp in temp_list:
    answer_dict[temp[0]] = index
    index -= 1 

answer = 0
for word in words:
    number = ''
    for letter in word:
        number += str(answer_dict[letter])
    answer += int(number)
print(answer)