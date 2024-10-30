import sys
input = sys.stdin.readline

n = int(input().strip())
list_box = []

for _ in range(n):
    x, y = map(int, input().strip().split())
    list_box.append((x, y))

list_box.sort()

for num in list_box:
    print(num[0], num[1])

