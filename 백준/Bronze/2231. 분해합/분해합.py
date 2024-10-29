import sys
input = sys.stdin.readline

# 주어진 수 m의 각 자리수를 더함
def sum_digit(m):
    tot = 0
    while m > 0:
        tot += m % 10
        m //= 10
    return tot

# n의 가장 작은 생성자 찾기
def find_smallest(n):
    start = max(1, n-9 * len(str(n)))

    for m in range(start, n):
        if m + sum_digit(m) == n:
            return m    # 생성자를 찾으면 m을 반환함
    return 0

n = int(input())
result = find_smallest(n)

print(result)

    