import sys
input = sys.stdin.readline

for _ in range(3):
    n = list(map(int, input().split()))
    back = n.count(0)

    if back == 1:
        print("A")
    elif back == 2:
        print("B")
    elif back == 3:
        print("C")
    elif back == 4:
        print("D")
    else:
        print("E")
