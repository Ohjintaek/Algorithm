import sys
input = sys.stdin.readline

racers = []
for _ in range(8):
    racers.append(list(input().split()))

racers.sort(key = lambda x : x[0])

R = []
B = []
scores = [10,8,6,5,4,3,2,1]
for i in range(8):
    if racers[i][1] == 'B':
        B.append(scores[i])
    if racers[i][1] == 'R':
        R.append(scores[i])

if (sum(B) > sum(R)):
    print("Blue")
elif (sum(B) < sum(R)):
    print("Red")
else:
    if (max(B) > max(R)):
        print("Blue")
    else:
        print("Red")