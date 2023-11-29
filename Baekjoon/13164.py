import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kids = list(map(int, input().split()))

btw_diff = dict()
for i in range(N-1):
    btw_diff[i] = kids[i+1] - kids[i]
sorted_btw_diff = sorted(btw_diff.items(), key=lambda x:x[1], reverse=True)

slices = []
for i in range(K-1):
    slices.append(sorted_btw_diff[i][0])
slices.sort()

answer = 0
index = 0
for i in range(K-1):
    answer += kids[slices[i]] - kids[index]
    index = slices[i]+1
answer += kids[N-1] - kids[index]

print(answer)