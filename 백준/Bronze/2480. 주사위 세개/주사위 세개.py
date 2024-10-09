import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

ans = 0 #0으로 초기화

#눈이 모두 같을 때
if A == B == C:
    ans = 10000 + A * 1000

#눈이 두 개만 같을 때
elif A == B or B == C or A == C:
    if A == B or A == C:
        ans = 1000 + A * 100
    else:
        ans = 1000 + B * 100

#눈이 모두 다를 때        
else:
    ans = max(A, B, C) * 100

print(ans)



