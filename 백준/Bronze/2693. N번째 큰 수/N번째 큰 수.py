import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a = list(map(int, input().split()))

    sorted_a = sorted(a, reverse=True)
    big_3 = sorted_a[2]

    print(big_3)
    
