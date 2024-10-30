import sys
input = sys.stdin.readline


n = int(input().strip())
list_box = []

for _ in range(n):
    x, y = map(int, input().strip().split())
    list_box.append((x, y))

#lamda => 익명 함수 생성 키워드. def키워드 사용하지 않고 한 줄로 간단하게 함수 구현하게 함.
list_box.sort(key=lambda num: (num[1], num[0]))

for num in list_box:
    print(num[0], num[1])

