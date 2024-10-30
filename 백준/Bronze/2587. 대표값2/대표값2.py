import sys
input = sys.stdin.readline

num_box = []

for _ in range(5):
    n = int(input().strip())
    num_box.append(n)

avg = sum(num_box) // 5

num_box.sort()  # 중앙값 추출 전 먼저 오름차순으로 정렬해야 함
middle = num_box[2]

print(avg)
print(middle)


