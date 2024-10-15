import sys
input = sys.stdin.readline

k = int(input().strip())
n_box = []

for _ in range(k):
    n = int(input().strip())

    if n == 0:
        if n_box:
            n_box.pop() # 가장 최근 수 제거 
    else:
        n_box.append(n)


print(sum(n_box))
