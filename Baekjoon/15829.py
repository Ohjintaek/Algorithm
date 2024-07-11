import sys
input = sys.stdin.readline
r, M = 31, 1234567891

L = int(input())
sentence = input().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
secretMap = dict()
for i in range(26):
    secretMap[alphabet[i]] = i+1

secretCode = 0
for i in range(L):
    secretCode += (secretMap[sentence[i]]*(r**i) % M)

secretCode %= M
print(secretCode)