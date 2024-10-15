import sys
input = sys.stdin.readline

n = int(input().strip())    # N의 진짜 약수 개수

divisor_box = list(map(int, input().split()))

N = min(divisor_box) * max(divisor_box)

print(N)
