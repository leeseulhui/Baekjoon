import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

tot = a * b * c

tot_str = str(tot)      # 결과를 문자열로 변경해주어야 함

count = [0] * 10

for digit in tot_str:
    count[int(digit)] += 1

for i in range(10):
    print(count[i])



