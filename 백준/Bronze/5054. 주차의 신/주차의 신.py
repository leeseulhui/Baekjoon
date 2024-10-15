import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input())    # 방문할 상점의 수
    location = list(map(int, input().split()))

    min_loc = min(location)
    max_loc = max(location)

    min_dis = 2 * (max_loc - min_loc)

    print(min_dis)
