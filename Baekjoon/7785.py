import sys
input = sys.stdin.readline

n = int(input())
commutes = set()
for _ in range(n):
    name, flag = input().split()
    if flag == "enter":
        commutes.add(name)
    else:
        commutes.remove(name)

commutes_name = list(commutes)
commutes_name.sort(reverse=True)

for name in commutes_name:
    print(name)