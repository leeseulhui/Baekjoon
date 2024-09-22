import sys
input = sys.stdin.readline

N = int(input())
i = 1

1 <= N <= 9

for i in range(1,10):
    tot = N * i
    print(f"{N} * {i} = {tot}")

    