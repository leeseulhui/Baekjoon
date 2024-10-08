import sys
input = sys.stdin.readline

def opt(value, opt):
    if opt == '@':
        return value * 3
    elif opt == '%':
        return value + 5
    elif opt == '#':
        return value -7

T = int(input().strip())

for _ in range(T):
    math = input().strip().split()
    result = float(math[0])

    for op in math[1:]:
        result = opt(result, op)

    print(f"{result:.2f}")


    