import sys
input = sys.stdin.readline

#입력부분
# 소수 : 1과 자신만으로만 나누어져야 함.
N = int(input())
numbers = list(map(int, input().split()))

#소수의 개수를 저장할 곳
prime = 0

for num in numbers:
    if num < 2:    #1은 소수가 아니기 때문에 건너뛰고 2부터 시작
        continue
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime = prime + 1

print(prime)