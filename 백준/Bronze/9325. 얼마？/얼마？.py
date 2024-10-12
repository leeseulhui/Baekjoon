import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    s = int(input().strip())    #기본 가격
    n = int(input().strip())    #옵션 개수

    tot_price = s

    for _ in range(n):
        q, p = map(int, input().split())
        tot_price += q * p

    print(tot_price)

