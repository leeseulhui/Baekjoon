import sys
input = sys.stdin.readline

N = int(input().strip())    #1번에서 N번방까지

if N == 1:
    print(1)

else:
    layer = 1
    count = 1

    while N > count:
        count = count + 6 * layer
        layer = layer + 1

    print(layer)