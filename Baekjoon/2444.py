import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, 2*N):
    stars = "*"*(min(2*i-1, 2*N-1-2*(i-N)))
    print(stars.center(2*N-1).rstrip())