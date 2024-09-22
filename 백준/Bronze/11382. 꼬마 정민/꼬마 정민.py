import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())         #input()으로 한 줄로 입력받고, split()을 사용해서 공백 기준으로 문자열 나눔.

1 <= A and C <= 10^12

sum = A + B + C

print(sum)



