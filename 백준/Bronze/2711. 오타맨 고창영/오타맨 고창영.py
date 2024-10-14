import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    miss, type = input().split()
    miss = int(miss)

    ans = type[:miss-1] + type[miss:]

    print(ans)

