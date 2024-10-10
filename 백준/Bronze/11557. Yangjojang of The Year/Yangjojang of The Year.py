import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())    # 학교의 숫자
    max_school = ""
    max_count = -1

    for _ in range(N):
        s, c = input().split()
        c = int(c)

        if c > max_count:
            max_count = c
            max_school = s
    
    print(max_school)


