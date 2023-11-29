import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))

students_score = [0 for _  in range(20001)]
for student in students:
    students_score[student + 10000] += 1

answer = 0
for i in range(N-1):
    for j in range(i+1,N):
        last_student = -(students[i] + students[j])
        if (last_student > 10000 or last_student < -10000):
            continue

        temp_answer = 0
        temp_answer += students_score[last_student + 10000]
        if (temp_answer > 0):
            if students[i] == last_student:
                temp_answer -= 1
            if students[j] == last_student:
                temp_answer -= 1
        answer += temp_answer

print(answer // 3)