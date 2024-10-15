import sys
input = sys.stdin.readline

sorted_box = []

for _ in range(5):
    n = int(input().strip())
    sorted_box.append(n)

avg = sum(sorted_box) // len(sorted_box)

sorted_box.sort()   # 리스트를 먼저 정렬
median = sorted_box[len(sorted_box) // 2]

print(avg)
print(median)