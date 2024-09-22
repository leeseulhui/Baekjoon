import sys
input = sys.stdin.readline


X = int(input())
N = int(input())

1 <= X <= 1000000000
1 <= N <= 100

tot = 0
for i in range(N):
    a,b = map(int, input().split())
    tot = tot + a*b

1 <= a <= 1000000
1 <= b <= 10

if tot == X:
    print("Yes")
else:
    print("No")

    
