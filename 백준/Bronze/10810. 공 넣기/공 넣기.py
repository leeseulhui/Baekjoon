import sys
input = sys.stdin.readline

N, M = map(int, input().split())    #N = 바구니 개수, M = 공을 넣는 횟수

basket = [0] * (N + 1)  #가장 처음 바구니에는 공이 들어있지 않기 때문에 0으로 초기화함

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        basket[idx] = k    

for num in range(1, N+1):  
    print(basket[num], end=' ')