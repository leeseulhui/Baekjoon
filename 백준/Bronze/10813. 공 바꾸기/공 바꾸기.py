import sys
input = sys.stdin.readline

N, M = map(int, input().split())    #N = 바구니 개수, M = 공을 넣는 횟수

basket = list(range(N+1))       #0번 인덱스 제외하고 1번부터 N번까지의 바구니 번호 가짐

for _ in range(M):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i] #서로 교환

print(" ".join(map(str, basket[1:])))
