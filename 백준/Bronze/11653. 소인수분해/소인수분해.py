import sys
input = sys.stdin.readline

N = int(input().strip())

if N == 1:
    exit()

for i in range(2, N + 1):
    while N % i == 0:
        print(i)
        N = N // i