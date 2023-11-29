import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    priority_with_index = []
    for i in range(N):
        priority_with_index.append((i, priority[i]))
    
    priority_max = max(priority)
    out_index = -1
    answer = 0
    
    while True:
        if priority_with_index[0][1] == priority_max:
            out = priority_with_index.pop(0)
            out_index = out[0]
            priority.remove(out[1])
            answer += 1

            if (out_index == M):
                break            

            priority_max = max(priority)
        else:
            priority_with_index.append(priority_with_index.pop(0))
    
    print(answer)        