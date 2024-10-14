import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input())

    position = 0

    result = []

    while n > 0:
        if n % 2 == 1:
            result.append(position)
        n //= 2
        position += 1

    print(' '.join(map(str, result)))
