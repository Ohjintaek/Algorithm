import sys
input = sys.stdin.readline

M = int(input())
times = []
for _ in range(M):
    h, m = map(int, input().split(":"))
    times.append((h-1)*60 + m)

max_R = 12*60
answer = M

for r in range(max_R):
    possible_times = set()

    for i in range(M):
        current_time = (times[i] - r*i) % max_R
        possible_times.add(current_time)

    answer = min(answer, len(possible_times))

print(answer)