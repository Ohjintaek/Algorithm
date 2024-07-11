import sys
input = sys.stdin.readline

for i in range(3):
    word = input().strip()
    if word.isnumeric():
        order, number = i, int(word)

target = number + 3 - order

if target % 15 == 0:
    print("FizzBuzz")
elif target % 5 == 0:
    print("Buzz")
elif target % 3 == 0:
    print("Fizz")
else:
    print(target)