import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set(map(int, input().split()))

b = set(map(int, input().split()))

# 대칭 차집합으로 원소 개수 계산
result = len(a.symmetric_difference(b))

print(result)