import sys
input = sys.stdin.readline

n = int(input().strip())    # 멀티탭 개수

tot_p = 0

for _ in range(n):
    p = int(input().strip())    # 꽂을 수 있는 플러그 수
    tot_p += p

max_p = tot_p - (n - 1)

print(max_p)

