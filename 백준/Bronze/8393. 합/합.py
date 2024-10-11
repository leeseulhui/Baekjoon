import sys
input = sys.stdin.readline

n = int(input().strip())
tot = 0

for i in range(1, n+1):
    tot += i

print(tot)
    