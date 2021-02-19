import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    students = []
    for i in range(N):
        total = 0
        mid, final, assign = map(int, input().split())
        total += mid * 0.35 + final * 0.45 + assign * 0.2
        students.append(total)
    students.sort(reverse=True)
    print(students)
    students.index(students[])




