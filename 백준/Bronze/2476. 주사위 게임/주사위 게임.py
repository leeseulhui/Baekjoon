import sys
input = sys.stdin.readline

N = int(input())
prize = []

for _ in range(N):
    a, b, c = map(int, input().split())

    if a == b == c:
        ans = 10000 + a * 1000
    elif a == b or a == c or b == c:
        if a == b or a == c:
            ans = 1000 + a * 100
        else:
            ans = 1000 + b * 100
    else:
        ans = max(a,b,c) * 100

    prize.append(ans)

print(max(prize))