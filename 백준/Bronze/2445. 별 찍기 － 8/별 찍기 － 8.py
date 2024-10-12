import sys
input = sys.stdin.readline

n = int(input().strip())

#상단
for i in range(1, n+1):
    star = '*' * i
    space = ' ' * (2 * (n - i))
    print(star + space + star)

#하단
for i in range(n-1, 0, -1):
    star = '*' * i
    sapce = ' ' * (2 * (n - i))
    print(star + sapce + star)

