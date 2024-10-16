import sys
input = sys.stdin.readline

def rev(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())

rev_x = rev(x)
rev_y = rev(y)

res = rev(rev_x + rev_y)

print(res)
