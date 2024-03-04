import sys
import heapq
input = sys.stdin.readline

N, k = map(int, input().split())
colors = input().strip()

records = dict()
previous_index = -1
start_index = 0
present_letter = colors[start_index]
present_count = 1
for i in range(1, N):
    if colors[i] != present_letter:
        if k >= (start_index+1) and k < (i+1):
            flag = start_index
        records[start_index] = [present_count, previous_index]
        previous_index = start_index
        start_index = i
        present_letter = colors[i]
        present_count = 0
    present_count += 1
records[start_index] = [present_count, previous_index]

heap = [(-records[record][0], record) for record in records]
heapq.heapify(heap)

answer = 0
while(True):
    answer += 1
    present_index = heapq.heappop(heap)[1]
    if present_index not in records:
        continue

    data = records.pop(present_index)
    if (present_index+1) <= k and (present_index + data[0] + 1) > k:
        break

    if data[1] in records and present_index + data[0] in records:
            if colors[data[1]] == colors[present_index + data[0]]:
                records[data[0]][0] += records[present_index + data[0]][0]
                records.pop(present_index + data[0])

                heapq.heappush(heap, (-records[data[0]][0], data[0]))