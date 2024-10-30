import sys
input = sys.stdin.readline

n = int(input().strip())
num_box = []

for _ in range(n):
    num = int(input().strip())
    num_box.append(num)

num_box.sort()

for num in num_box:
    print(num)




