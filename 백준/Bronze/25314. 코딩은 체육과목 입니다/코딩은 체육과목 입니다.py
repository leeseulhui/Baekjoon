import sys
input = sys.stdin.readline


N = int(input())

4 <= N <= 1000 and N % 4

long = N // 4

result = "long " * long + "int"

print(result.strip())