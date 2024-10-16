import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):

    n_box = []
    n = list(map(int, input().split()))

    for num in n:
        if num % 2 == 0:
            n_box.append(num)

    n_sum = sum(n_box)
    n_min = min(n_box)

    print(n_sum, n_min)
    
