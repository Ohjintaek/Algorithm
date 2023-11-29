import sys
input = sys.stdin.readline

def mult(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

N = int(input())
flowers = list(map(int, input().split()))

i,j,k = 1,2,3
answer = 1

while (i < N - 2):
    answer = max(answer, mult(flowers[:i]) + mult(flowers[i:j]) + mult(flowers[j:k]) + mult(flowers[k:]))
    if (k < N - 1):
        k += 1
        continue
    elif (j < N - 2):
        j += 1
        continue
    else:
        i += 1
        j = i + 1
        k = j + 1
        continue

print(answer)