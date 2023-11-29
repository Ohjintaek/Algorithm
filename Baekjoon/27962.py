import sys
input = sys.stdin.readline

N = int(input())
word = input().strip()

def count_difference(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

answer = "NO"
for i in range(1, N):
    if count_difference(word[:i], word[N-i:]) == 1:
        answer = "YES"
        break

print(answer)