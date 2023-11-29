import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
traffic_light = [1 for _ in range(N)]
for _ in range(B):
    traffic_light[int(input()) - 1] = 0

cumul_sum = [traffic_light[0]]
for i in range(1,N):
    cumul_sum.append(cumul_sum[i-1] + traffic_light[i])
cumul_sum.append(0)

answer = N
for i in range(N-K+1):
    to_fix = K - (cumul_sum[i+K-1] - cumul_sum[i-1])
    answer = min(answer, to_fix)

print(answer)