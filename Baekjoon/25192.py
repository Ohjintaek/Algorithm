import sys
input = sys.stdin.readline

N = int(input())
answer = 0
people = set()
for _ in range(N):
    word = input().strip()
    if word == "ENTER":
        answer += len(people)
        people.clear()
        continue
    people.add(word)
answer += len(people)
print(answer)