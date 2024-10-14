import sys
input = sys.stdin.readline

max_score = 0
winner = 0

for i in range(5):
    score = list(map(int, input().split()))

    tot = sum(score)

    if tot > max_score:
        max_score = tot
        winner = i + 1
   
print(winner, max_score)
   



