import sys
input = sys.stdin.readline

N = [int(input().strip())for _ in range(9)]

#최댓값 구해
max_value = max(N)

#최댓값 위치 구해
max_index = N.index(max_value) + 1    #1부터 시작하는 인덱스이므로 +1이 필요

print(max_value)
print(max_index)
