import sys
input = sys.stdin.readline

#시험 본 과목의 개수
N = int(input().strip())

#업데이트 전 과목 시험 점수(현재 성적)
score = list(map(int, input().split()))

M = max(score)

update_score = [(s / M) * 100 for s in score]
new_avg = sum(update_score) / N

print(new_avg)

