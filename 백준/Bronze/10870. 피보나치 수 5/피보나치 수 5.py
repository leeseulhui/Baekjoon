import sys
input = sys.stdin.readline

n = int(input().strip())

f = [0, 1]

for num in range(2, n+1):
    f.append(f[num-1] + f[num-2])

print(f[n])
