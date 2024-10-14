import sys
input = sys.stdin.readline

start, end = map(int, input().split())

num = []
for i in range (1, 1001):
    num.extend([i] * i) #숫자 i를 i번 리스트에 추가하겠다

result = sum(num[start-1:end])

print(result)
    