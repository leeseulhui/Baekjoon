import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    v, e = map(int, input().split())

    space = 2 - (v - e)

    print(space)