import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = [0 for _ in range(12)]
temp[1] = 1
temp[2] = 2
temp[3] = 4
for i in range(4, 12):
    temp[i] = temp[i-3] + temp[i-2] + temp[i-1]

answer_set = [[[1]],[[1,1],[2]],[[1,1,1],[1,2],[2,1],[3]]]

if k > temp[n]:
    print(-1)

elif n <= 3:
    print(*answer_set[n-1][k-1], sep = '+')

else:
    answer_sum = []
    while(n > 3):
        if (k <= temp[n-1]):
            answer_sum.append(1)
            n -= 1
        elif (k <= temp[n-1] + temp[n-2]):
            answer_sum.append(2)
            k -= temp[n-1]
            n -= 2
        else:
            answer_sum.append(3)
            k -= (temp[n-1] + temp[n-2])
            n -= 3
    answer_sum.extend(answer_set[n-1][k-1])
    print(*answer_sum, sep = '+')