import sys
input = sys.stdin.readline

N = int(input())
members = []
for _ in range(N):
    members.append(list(map(str, input().split())))

members.sort(key = lambda x : int(x[0]))
for age, name in members:
    print(age, name)