import sys
input = sys.stdin.readline

S = input().strip()

if len(S) == 1:
    start, end = S, S
elif len(S) == 2:
    if int(S[0]) + 1 == int(S[1]):
        start = S[0]
        end = S[1]
    else:
        start, end = S, S
elif len(S) == 3:
    if int(S[0]) + 1 == int(S[1]):
        if int(S[1]) + 1 == int(S[2]):
            start = S[0]
            end = S[2]
        else:
            start, end = S, S
    elif S == '910':
        start, end = 9, 10
    else:
        start, end = S, S 
else:
    for i in range(1, 1000):
        if str(i)[0] == S[0]:
            temp = ''
            for j in range(i, 1000):
                temp += str(j)
                if temp == S:
                    start, end = i, j

print(start, end)