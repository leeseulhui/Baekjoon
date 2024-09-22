import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

2 <= A and C <= 10000

x = (A+B)%C
y = ((A%C) + (B%C))%C
z = (A*B)%C
o = ((A%C)*(B%C))%C

print(x)
print(y)
print(z)
print(o)

