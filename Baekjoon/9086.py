import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().strip()
    print("{}{}".format(S[0], S[len(S)-1]))