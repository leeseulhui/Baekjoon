import sys
input = sys.stdin.readline

canvas = [[0] * 100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            canvas[i][j] = 1

black = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            black = black + 1

print(black)
    

   
