import sys
input = sys.stdin.readline

w_score = []
for _ in range(10):
    w_s = int(input().strip())
    w_score.append(w_s)

sorted_w = sorted(w_score, reverse=True)
sum_w = sum(sorted_w[:3])


k_score = []
for _ in range(10):
    k_s = int(input().strip())
    k_score.append(k_s)

sorted_k = sorted(k_score, reverse=True)
sum_k = sum(sorted_k[:3])

print(sum_w, sum_k)