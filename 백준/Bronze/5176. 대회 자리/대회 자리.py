import sys
input = sys.stdin.readline

k = int(input().strip())

for _ in range(k):
    p, m = map(int, input().split())
    seats = [0] * (m + 1)
    no_part = 0

    for _ in range(p):
        seat = int(input().strip())
        if seats[seat] == 0:    # 아무도 자리에 앉지 않았다면
            seats[seat] = 1 # 자리에 앉는다.
        else:
            no_part += 1    # 이미 자리가 차있으면 참가 못함

    print(no_part)
