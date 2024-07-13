import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    minHeap = []
    maxHeap = []
    length = 0
    for _ in range(k):
        operator, operand = input().split()
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(minHeap, operand)
            heapq.heappush(maxHeap, (-operand, operand))
            length += 1
        else:
            if length == 0:
                continue
            if operand == -1:
                heapq.heappop(minHeap)
            else:
                heapq.heappop(maxHeap)

            length -= 1
            if length == 0:
                minHeap.clear()
                maxHeap.clear()

    if length:
        print(maxHeap[0][1], minHeap[0])
    else:
        print('EMPTY')