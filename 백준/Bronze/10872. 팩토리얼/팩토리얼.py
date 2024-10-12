import sys
input = sys.stdin.readline

N = int(input().strip())
tot = 1

for i in range(1,N+1):
    tot *= i
print(tot)