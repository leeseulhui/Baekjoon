import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1, N+1):
    print(' ' * (i - 1) + '*' * (N - i + 1))