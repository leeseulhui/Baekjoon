import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().split(","))

    sum = a+b
    print(sum)



