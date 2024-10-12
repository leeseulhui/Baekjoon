import sys
input = sys.stdin.readline

sum = 0

for _ in range(5):
    n = int(input().strip())
    sum += n

print(sum)
