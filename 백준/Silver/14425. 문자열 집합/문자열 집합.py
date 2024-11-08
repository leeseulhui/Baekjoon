import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s_set = set()
for _ in range(n):
    s_set.add(input().strip())

cnt = 0
for _ in range(m):
    words = input().strip()
    if words in s_set:
        cnt += 1

print(cnt)
