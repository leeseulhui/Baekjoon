import sys
input = sys.stdin.readline

A, B = input().split()

#숫자 거꾸로 뒤집어
reversed_A = A[::-1]
reversed_B = B[::-1]


reversed_A = int(reversed_A)
reversed_B = int(reversed_B)

answer = max(reversed_A, reversed_B)
print(answer)
