# 피보나치를 반복문으로 풀면 효율적 but 간단한 구현은 재귀함수임. 그러나 재귀는 성능이 반복문보다 떨어짐. 
# 해결법은 메모이제이션을 사용하는 것!

import sys
input = sys.stdin.readline

memo = {}

def fibo(n):
    if n in memo: # 피보나치 계산값이 이미 메모제이션 리스트에 저장되어 있다면
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())

print(fibo(n))
