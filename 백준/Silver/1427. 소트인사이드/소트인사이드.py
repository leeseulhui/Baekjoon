import sys
input = sys.stdin.readline

n = input().strip()

sorted_n = sorted(n, reverse=True)

print(''.join(sorted_n))