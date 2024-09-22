import sys
input = sys.stdin.readline


n = int(input())
1<= n <= 10000
sum = 0

for i in range(1, n + 1):
    sum = i + sum
print(sum)