import sys
input = sys.stdin.readline

S, E, R = map(str, input().split())
S = int(S.replace(":", ""))
E = int(E.replace(":", ""))
R = int(R.replace(":", ""))
start_participants = set()
end_participants = set()

while True:
    try:
        time, nickname = map(str, input().split())
        time = int(time.replace(":", ""))
        if (time <= S):
            start_participants.add(nickname)
        if (time >= E) and (time <= R):
            end_participants.add(nickname)
    except:
        break

participants = set.intersection(start_participants, end_participants)
print(len(participants))