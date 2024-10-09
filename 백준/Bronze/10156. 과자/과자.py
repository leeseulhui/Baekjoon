import sys
input = sys.stdin.readline

K, N, M = map(int, input().split())

pay = K * N
need = pay - M

if need < 0:
    need = 0

    
print(need)