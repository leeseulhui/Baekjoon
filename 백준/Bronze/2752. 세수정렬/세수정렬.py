import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

sorted_n = sorted(n)

print(' '.join(map(str, sorted_n)))
 