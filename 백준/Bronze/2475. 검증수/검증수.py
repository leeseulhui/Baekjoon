import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

n_sum = sum(num ** 2  for num in n)

ans = n_sum % 10

print(ans)

