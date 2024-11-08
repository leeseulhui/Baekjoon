import sys
input = sys.stdin.readline
import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

baby = a1 * b2 + a2 * b1       #분자
mom = b1 * b2

gcd = math.gcd(baby, mom)
baby //= gcd
mom //= gcd

print(baby, mom)

