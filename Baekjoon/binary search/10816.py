import sys
import bisect

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    print(bisect.bisect_right(cards, number) - bisect.bisect_left(cards, number), end = ' ')