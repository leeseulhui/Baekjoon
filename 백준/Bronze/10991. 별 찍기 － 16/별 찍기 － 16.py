import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print(" "*(N-i), end="")    # 첫 줄 * 시작 전 공백
    for j in range(i-1):
        print('*', end=" ") 
    print("*")
