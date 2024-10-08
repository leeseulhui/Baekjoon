import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())
need = int(input().strip())

#총 필요한 요리시간
C = C + need

B = B + C // 60
C = C % 60

#분이 60이 넘어갔다.
A = A + B // 60
B = B % 60

#시가 24시를 넘겼다.
A = A % 24

print(A, B, C)