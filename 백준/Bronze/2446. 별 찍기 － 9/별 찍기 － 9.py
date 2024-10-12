import sys
input = sys.stdin.readline

n = int(input().strip())

#상단
for i in range(n):
    star = '*' * (2 * (n - i) - 1)
    space = ' ' * i
    print(space + star)

#하단
for i in range(1, n):
    star = '*' * (2 * i + 1) 
    space = ' ' * (n - i - 1)
    print(space + star)




