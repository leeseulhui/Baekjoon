import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 도감에 있는 포켓몬 개수 / 맞춰야 하는 문제 개수

# 문자인 상황 / 숫자인 상황의 딕셔너리 각각 초기화
name_num = {}
number_num = {}

for i in range(1, n+1):
    pocket_name = input().strip()
    name_num[pocket_name] = i
    number_num[i] = pocket_name

for _ in range(m):
    query = input().strip()
    if query.isdigit():    # 만약 query가 숫자라면?
        print(number_num[int(query)])
    else:   # 문자라면?
        print(name_num[query])

