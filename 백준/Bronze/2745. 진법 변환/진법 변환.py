import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)

#N을 B진법에서 10진법으로 변환
result = int(N, B)
print(result)

   
