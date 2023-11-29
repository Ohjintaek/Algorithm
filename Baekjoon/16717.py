import sys
import re
input = sys.stdin.readline

S = input().strip()
K = input().strip()

origin_word = re.sub('[0-9]', '', S)
if (origin_word.find(K) >= 0):
    print(1)
else:
    print(0)