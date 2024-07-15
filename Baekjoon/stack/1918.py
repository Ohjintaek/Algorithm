import sys
input = sys.stdin.readline

priority = dict()
priority['+'] = 1
priority['-'] = 1
priority['*'] = 2
priority['/'] = 2
priority['('] = 0

# A*(B+C)+D
# ABC+*D+
# 자신보다 더 낮은 우선순위의 연산자가 스택에 들어올 때 같거나 더 높은 우선순위를 가지는 연산자를 스택에서 빼낸다.
# 즉, 스택에서 왼쪽에는 항상 자신보다 더 높은 우선순위를 가지는 연산자만 남아야 한다.
# 단, 여는 괄호가 등장했을 때는 바로 스택에 넣는다.
# 괄호가 스택에서 제거될 때는 최종 문자열에는 포함시키지 않는다.

inOrder = input().strip()
stack = []
answer = ''
for letter in inOrder:
    if letter == '(':
        stack.append(letter)
    elif letter == ')':
        while stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    elif letter in priority:
        while stack and priority[stack[-1]] >= priority[letter]:
            answer += stack.pop()
        stack.append(letter)
    else:
        answer += letter

while stack:
    answer += stack.pop()

print(answer)