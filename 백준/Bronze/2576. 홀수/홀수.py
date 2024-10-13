import sys
input = sys.stdin.readline

ans = []    #홀수들 저장할 리스트


for _ in range(7):
    n = int(input().strip())
    if n % 2 == 1:
        ans.append(n)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))

