import sys
input = sys.stdin.readline

p_box = []

n = int(input().strip())

for _ in range(n):
    p = int(input().strip())

    p_box.append(p)

    sorted_p = sorted(p_box)

for num in sorted_p:
    print(num)