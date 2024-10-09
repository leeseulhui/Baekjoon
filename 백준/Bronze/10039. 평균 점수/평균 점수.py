import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range(5)]

under_score = []

for score in scores:
    if score < 40:
        under_score.append(40)
    else:
        under_score.append(score)

avg_score = sum(under_score) // len(under_score)

print(avg_score)