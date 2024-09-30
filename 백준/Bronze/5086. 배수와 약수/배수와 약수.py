import sys
input = sys.stdin.readline

# 입력부분

while True:
    one, two = map(int, input().split())

    if one ==0 and two ==0:
        break

    if two % one == 0:
        print("factor")
    elif one % two == 0:
        print("multiple")
    else:
        print("neither")

