import sys
input = sys.stdin.readline

# 그리디로 해결!
# 5kg 우선 사용 -> 나머지는 3kg 사용

n = int(input())

count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5 # 5kg 를 최대한 사용하자
        print(count)
        break
    
    n -= 3  # 5로 나누어 떨어지지 않으면
    count += 1 #3키로 사용
else:
    print(-1)

