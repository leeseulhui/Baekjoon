import sys
input = sys.stdin.readline

n = int(input().strip())
cards = set(map(int, input().split()))  # set을 해준 이유: 문제 조건 중 '두 숫자 카드에 같은 수가 적혀있는 경우는 없다.' 

m = int(input().strip())    
check_nums = list(map(int, input().split()))

result = []

for num in check_nums:
    if num in cards:     # 만약 num이 cards 리스트에 존재한다면?
        result.append("1")
    else:
        result.append("0")

print(" ".join(result))


