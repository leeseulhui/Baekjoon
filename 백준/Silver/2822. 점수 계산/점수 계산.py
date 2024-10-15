import sys
input = sys.stdin.readline

score_box = []
for _ in range(8):
    score = int(input().strip())
    score_box.append(score)

# 최대 5개니까 먼저 리스트를 내림차순으로 정렬
sorted_score = sorted(score_box, reverse=True)
top_5 = sorted_score[:5]

tot = sum(top_5)


# 어떤 문제가 있는지 탐색
select_p = []
for i in range(8):
    if score_box[i] in top_5:
        select_p.append(i + 1)

select_p.sort() # 오름차순 정렬

print(tot)
print(' '.join(map(str, select_p)))


