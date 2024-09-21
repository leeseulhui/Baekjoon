import sys
input = sys.stdin.readline

n = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(n)]

pillars.sort()

max_height = 0
max_idx = 0
for i in range(n):
    if pillars[i][1] > max_height:  
        max_height = pillars[i][1] 
        max_idx = i

area = 0
left_height = pillars[0][1]
for i in range(max_idx):
    if pillars[i][1] > left_height:
        left_height = pillars[i][1]
    area += left_height * (pillars[i + 1][0] - pillars[i][0])

right_height = pillars[-1][1]
for i in range(n - 1, max_idx, -1):
    if pillars[i][1] > right_height:
        right_height = pillars[i][1]
    area += right_height * (pillars[i][0] - pillars[i - 1][0])

area += max_height

print(area)
