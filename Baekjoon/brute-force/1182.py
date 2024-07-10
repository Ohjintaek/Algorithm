import sys
input = sys.stdin.readline

def solution(sum, index):
    global answer
    if index == N:
        return
    
    solution(sum, index+1)
    tempSum = sum + numbers[index]
    if tempSum == S:
        answer += 1
    solution(tempSum, index+1)

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
solution(0, 0)

print(answer)