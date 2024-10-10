import sys
input = sys.stdin.readline

n = int(input().strip())

a_score = 100
b_score = 100

for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        b_score -= a

    elif a < b:
        a_score -= b

print(a_score)
print(b_score)

