import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if 1 <= A <= 10000 and 1 <= B <= 10000:

    sum = A + B
    min = A - B
    double = A * B
    div = A // B
    mod = A % B

print(sum)
print(min)
print(double)
print(div)
print(mod)