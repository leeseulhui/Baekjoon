import sys
input = sys.stdin.readline

n = int(input().strip())
current_score = list(map(int, input().split()))

m = max(current_score)  # 자기 점수 중 최댓값

re_score = [(score / m) * 100 for score in current_score]

avg = sum(re_score) / n

print(avg)

