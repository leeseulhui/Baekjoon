import sys
input = sys.stdin.readline

n = int(input().strip())
score = list(map(int, input().split()))

tot_score = 0
plus_score = 0

for s in score:
    if s == 1:
        plus_score += 1
        tot_score += plus_score
    else:
        plus_score = 0

print(tot_score)

