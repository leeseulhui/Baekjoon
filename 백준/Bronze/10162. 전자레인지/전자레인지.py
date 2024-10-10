import sys
input = sys.stdin.readline

T = int(input().strip())

a = 300
b = 60
c = 10

# 최소 10이 되어야함. > 왜? 버튼들이 모두 10의 배수임, 10으로 나누어 떨어지지 않으면 버튼으로 맞출 수가 없음
if T % 10 != 0:
    print(-1)

else:
    count_a = T // a
    T %= a

    count_b = T // b
    T %= b

    count_c = T // c

    print(count_a, count_b, count_c)

