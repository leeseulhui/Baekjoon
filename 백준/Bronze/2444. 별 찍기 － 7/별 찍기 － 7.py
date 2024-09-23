import sys
input = sys.stdin.readline

N = int(input().strip())

# 위쪽 삼각형
for i in range(1, N + 1):
    spaces = ' ' * (N - i) 
    stars = '*' * (2 * i - 1) 
    print(spaces + stars)

# 아래쪽 삼각형
for i in range(N + 1, 2 * N):
    spaces = ' ' * (i - N) 
    stars = '*' * (2 * (2 * N - i) - 1)
    print(spaces + stars)