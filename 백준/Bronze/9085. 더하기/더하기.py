import sys
input = sys.stdin.readline

t = int(input().strip())

n_sum = 0

for _ in range(t):
    n = int(input().strip())
    num = map(int, input().split())

    n_sum = sum(num)

    print(n_sum)