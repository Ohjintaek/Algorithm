import sys
input = sys.stdin.readline

def func(N, words):
    if N == 0:
        return words
    a, b, c = func(N-1, words[:3**(N-1)]), " "*3**(N-1), func(N-1, words[2*3**(N-1):])
    return a+b+c



while(True):
    N = input()
    if not N:
        break
    N = int(N)
    words = "-"*3**N
    answer = func(N, words)
    print(answer)
