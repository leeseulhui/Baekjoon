import sys
input = sys.stdin.readline

A, B = map(int, input().split())

div = A / B
print(f"{div:.9f}")
