import sys
input = sys.stdin.readline

credit_sum = 0
score_sum = 0
for _ in range(20):
    subject, credit, score = input().split()
    credit = float(credit)

    if score == "A+":
        credit_sum += credit
        score_sum += credit*4.5
    elif score == "A0":
        credit_sum += credit
        score_sum += credit*4.0
    elif score == "B+":
        credit_sum += credit
        score_sum += credit*3.5
    elif score == "B0":
        credit_sum += credit
        score_sum += credit*3.0
    elif score == "C+":
        credit_sum += credit
        score_sum += credit*2.5
    elif score == "C0":
        credit_sum += credit
        score_sum += credit*2.0
    elif score == "D+":
        credit_sum += credit
        score_sum += credit*1.5
    elif score == "D0":
        credit_sum += credit
        score_sum += credit*1.0
    elif score == "F":
        credit_sum += credit
    
print(score_sum / credit_sum)
