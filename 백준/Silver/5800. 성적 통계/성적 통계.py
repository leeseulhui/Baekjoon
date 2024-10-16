import sys
input = sys.stdin.readline

c = int(input().strip())

for c_num in range(1, c + 1):
    stu = list(map(int, input().split()))

    n = stu[0]
    score = stu[1:]

    max_score = max(score)
    min_score = min(score)

    sorted_score = sorted(score, reverse=True)

    largest_gap = 0
    for i in range(1, n):
        gap = sorted_score[i - 1] - sorted_score[i]
        largest_gap = max(largest_gap, gap)

    print(f"Class {c_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")

  
