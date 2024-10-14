import sys
input = sys.stdin.readline

a, b = input().split()

# 숫자 뒤집기
a_reverse = a[::-1]
b_reverse = b[::-1]

a_reverse = int(a_reverse)
b_reverse = int(b_reverse)

ans = max(a_reverse, b_reverse)
print(ans)