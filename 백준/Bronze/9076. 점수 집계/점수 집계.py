import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    score = list(map(int, input().split()))

    max_score = max(score)
    min_score = min(score)

    # 나머지 3개 점수 남기기
    remain_3 = score[:]

    remain_3.remove(max_score)
    remain_3.remove(min_score)

    if max(remain_3) - min(remain_3) >= 4:
        print("KIN")
    else:
        print(sum(remain_3))




