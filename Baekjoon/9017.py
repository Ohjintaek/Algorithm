import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    team_count = [0 for _ in range(201)]
    for team in teams:
        team_count[team] += 1
    
    deserve_team = []
    for i in range(1,201):
        if team_count[i] == 6:
            deserve_team.append(i)

    score = 1
    scores = [[] for _ in range(201)]
    for team in teams:
        if team in deserve_team:
            scores[team].append(score)
            score += 1
    
    answer = deserve_team[0]
    answer_score = sum(scores[answer][:4])

    for i in range(1, len(deserve_team)):
        team_index = deserve_team[i]
        temp_score = sum(scores[team_index][:4])
        if temp_score < answer_score:
            answer = team_index
            answer_score = temp_score
        elif temp_score == answer_score:
            if scores[team_index][4] < scores[answer][4]:
                answer = team_index
    
    print(answer)