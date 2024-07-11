import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

length = 2*N + 1

answer = 0
flag = False
prev = ''
count = 0
for i in range(M):
    if S[i] == 'I':
        if not flag:
            flag = True
            prev = 'I'
            count = 1
        else:
            if prev == 'I':
                if count >= length:
                    answer += (count - length)//2 + 1
                count = 1
            else:
                prev = 'I'
                count += 1
    else:
        if flag:
            if prev == 'I':
                prev = 'O'
                count += 1
            else:
                if count >= length:
                    answer += (count - length)//2 + 1
                flag = False
                count = 0

if count >= length:
    answer += (count-length)//2 + 1

print(answer)