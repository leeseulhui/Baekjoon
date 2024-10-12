import sys
input = sys.stdin.readline

N = int(input().strip())
p = 0

# N개의 수 입력받을 리스트
num = list(map(int, input().split()))

for n in num:
    if n < 2:
        continue

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        p += 1

print(p) 


    