import sys
input = sys.stdin.readline

n, k = map(int, input().split())
m_sum = 0

coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0

for value in reversed(coins):
    if k == 0:
        break
    count += k // value
    k %= value

print(count)


