import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    minHeap = []
    maxHeap = []
    queueDetail = dict()
    length = 0
    for _ in range(k):
        operator, operand = input().split()
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(minHeap, operand)
            heapq.heappush(maxHeap, (-operand, operand))
            length += 1

            if operand not in queueDetail:
                queueDetail[operand] = 1
            else:
                queueDetail[operand] += 1
        else:
            if length == 0:
                continue
            if operand == -1:
                while queueDetail[minHeap[0]] == 0:
                    heapq.heappop(minHeap)
                target = heapq.heappop(minHeap)
            else:
                while queueDetail[maxHeap[0][1]] == 0:
                    heapq.heappop(maxHeap)
                target = heapq.heappop(maxHeap)[1]
            length -= 1
            queueDetail[target] -= 1
    
    if length:
        while queueDetail[minHeap[0]] == 0:
            heapq.heappop(minHeap)
        _min = minHeap[0]

        while queueDetail[maxHeap[0][1]] == 0:
            heapq.heappop(maxHeap)
        _max = maxHeap[0][1]
        print(_max, _min)
    else:
        print('EMPTY')