import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 집합 s에 포함된 문자열을 set에 저장시킴
s_set = set()
for _ in range(n):
    s_set.add(input().strip())

count = 0
for _ in range(m):
    words = input().strip()
    if words in s_set:
        count += 1

print(count)

