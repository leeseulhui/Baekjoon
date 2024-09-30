import sys
input = sys.stdin.readline

# 입력부분
A, B, V = map(int, input().split())

day = (V - B) // (A - B)

if (V - B) % (A - B) != 0:  # 나머지가 0이 아니라는 것은 하루를 더 가야한다는 뜻이기 때문에 day + 1 해주어야함
    day = day + 1

print(day)

