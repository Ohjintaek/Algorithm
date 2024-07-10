import sys
input = sys.stdin.readline

N = int(input())
heights = []
for _ in range(N):
    heights.append(int(input()))

answer = 0

# 스택에 막대를 추가할 때 가장 마지막에 추가된 막대의 높이보다 같거나 높다면 오른쪽으로 확장할 수 있다.
# 하지만 그렇지 않으면 거기까지이므로 새로 추가될 막대까지 확장할 수 있는 위치까지 스택에서 꺼낸다.
stack = []
for i in range(N):
    index = i
    while stack and stack[-1][1] > heights[i]:
        index, height = stack.pop()
        area = (i - index) * height
        answer = max(answer, area)
    # 스택에 막대를 저장할 때 왼쪽으로 어디까지 확장할 수 있는지 index에 저장
    stack.append([index, heights[i]])

while stack:
    index, height = stack.pop()
    area = (N - index) * height
    answer = max(answer, area)

print(answer)