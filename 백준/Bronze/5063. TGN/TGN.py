import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    r, e, c = map(int, input().split())

    if e - c > r:
        ans = "advertise"
    elif e - c < r:
        ans = "do not advertise"
    else:
        ans = "does not matter"


    print(ans)
