import sys
input = sys.stdin.readline

students = [i + 1 for i in range(30)]

for _ in range(28):
    students.remove(int(input()))

for student in students:
    print(student)