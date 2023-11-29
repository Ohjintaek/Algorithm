import sys
from heapq import *
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    heapify(pages)
    answer = 0

    while(len(pages) > 1):
        temp_sum = heappop(pages) + heappop(pages)
        answer += temp_sum
        heappush(pages, temp_sum)
    
    print(answer)