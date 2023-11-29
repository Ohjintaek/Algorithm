import sys
input = sys.stdin.readline

def func(n):
    for i in range(len(S)-n+1):
        left_sum = cumul_sum[i+(n//2)-1] - cumul_sum[i-1]
        right_sum = cumul_sum[i+n-1] - cumul_sum[i+(n//2)-1]
        if left_sum == right_sum:
            return True
    return False


S = list(map(int, input().strip()))
cumul_sum = [S[0]]
for i in range(1, len(S)):
    cumul_sum.append(cumul_sum[i-1] + S[i])
cumul_sum.append(0)

flag = False
length = 1000
while not flag:
    if func(length):
        flag = True
    else:
        length -= 2

print(length)