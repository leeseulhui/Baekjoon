import sys
input = sys.stdin.readline

n = int(input().strip())

check_box = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        check_box.add(name)
    elif status == "leave":
        check_box.remove(name)

for name in sorted(check_box, reverse=True):
    print(name)
