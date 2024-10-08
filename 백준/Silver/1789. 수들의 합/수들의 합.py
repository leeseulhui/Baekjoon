import sys
input = sys.stdin.readline

S = int(input().strip())

N = 0
sum = 0

while True:
    N = N+1
    sum = sum + N

    if sum > S:
        break

print(N-1)

