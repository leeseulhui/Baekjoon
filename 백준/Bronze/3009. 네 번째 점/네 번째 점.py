import sys
input = sys.stdin.readline
# x, y 좌표의 수가 각각 2개씩 존재하면 되는 것임

points = []

for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

x_point = [point[0] for point in points]
y_point = [point[1] for point in points]

# 네 번째 점의 x 좌표
if x_point.count(x_point[0]) == 1:
    four_x = x_point[0]
elif x_point.count(x_point[1]) == 1:
    four_x = x_point[1]
else:
    four_x = x_point[2]

# 네 번째 점의 y 좌표
if y_point.count(y_point[0]) == 1:
    four_y = y_point[0]
elif y_point.count(y_point[1]) == 1:
    four_y = y_point[1]
else:
    four_y = y_point[2]

print(f"{four_x} {four_y}")


