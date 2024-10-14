import sys
input = sys.stdin.readline

n = int(input().strip())

car_num = list(map(int, input().split()))

ans = 0

for car in car_num:
        if car == n:
                
                ans += 1

print(ans)
   

