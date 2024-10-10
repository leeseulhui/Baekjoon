import sys
input = sys.stdin.readline

N = int(input().strip())

min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')

for _ in range(N):
    x, y = map(int, input().split())

    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

width = max_x - min_x
height = max_y - min_y

print(width * height)
    
