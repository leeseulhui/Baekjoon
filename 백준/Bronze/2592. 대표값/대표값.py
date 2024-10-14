import sys
input = sys.stdin.readline
from collections import Counter

num = []

for _ in range(10):
    a = int(input().strip())
    num.append(a)
    
avg = sum(num) // 10

count = Counter(num)
max_num = count.most_common(1)[0][0]    # 가장 빈도가 높은 것을 튜플형태로 가지고옴

print(avg)
print(max_num)

