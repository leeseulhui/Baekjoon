import sys
input = sys.stdin.readline

grade_to_score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

tot_score = 0   #(학점 * 과목 평점)의 총합
tot_credits = 0     #학점 총합

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade == 'P':
        continue

    #총 학점에 더하기
    tot_credits = tot_credits + credit

    #과목의 학점 * 평점
    tot_score = tot_score + credit  * grade_to_score[grade]

#전공 평점
major = tot_score / tot_credits

print(f"{major:.6f}")