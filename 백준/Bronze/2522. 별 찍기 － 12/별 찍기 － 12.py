import sys
input = sys.stdin.readline

n = int(input().strip())

# 상단
for i in range(1, n):
    print(' '*(n-i)+'*'*i)

# 하단
for i in range(n, 0, -1):
    print(' '*(n-i)+'*'*i)