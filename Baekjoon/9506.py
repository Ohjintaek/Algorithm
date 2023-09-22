import sys
input = sys.stdin.readline
default_sentence = " is NOT perfect."

while (True):
    n = int(input())
    if (n == -1):
        break

    temp = []
    for i in range(1, n//2 + 1):
        if (n % i == 0):
            temp.append(i)
    
    if (sum(temp) == n):
        print(str(n) + " = ", end = "")
        print(*temp, sep = " + ")
    else:
        print(str(n), end = "")
        print(default_sentence)