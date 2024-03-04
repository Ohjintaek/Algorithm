import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    numbers = []
    for _ in range(M//10 + 1):
        numbers.extend(list(map(int, input().split())))

    answer = []
    left_heap = [] # 최대 힙
    right_heap = [] # 최소 힙
    diff = 0

    # left_heap의 원소 갯수 - right_heap의 원소 갯수(diff)가 항상 1 이내가 되도록 유지
    for i in range(M):
        if i == 0:
            heapq.heappush(left_heap, (-numbers[i], numbers[i]))
        elif i == 1:
            if left_heap[0][1] < numbers[i]:
                heapq.heappush(right_heap, numbers[i])
            else:
                heapq.heappush(right_heap, heapq.heappushpop(left_heap, (-numbers[i], numbers[i]))[1])
        else:
            if diff == 0:
                target = heapq.heappushpop(right_heap, numbers[i])
                heapq.heappush(left_heap, (-target, target))
                diff = 1
            else:
                target = heapq.heappushpop(left_heap, (-numbers[i], numbers[i]))
                heapq.heappush(right_heap, target[1])
                diff = 0

        if i % 2 == 0:
            answer.append(left_heap[0][1])

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=' ')
        if i % 10 == 9:
            print()
    print()