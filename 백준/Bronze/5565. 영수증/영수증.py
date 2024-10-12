import sys
input = sys.stdin.readline


t_price = int(input().strip())  #10권의 총 가격
n_sum = 0   #9권의 합

for _ in range(9):

    n_sum += int(input().strip())

m_price = t_price - n_sum   

print(m_price)