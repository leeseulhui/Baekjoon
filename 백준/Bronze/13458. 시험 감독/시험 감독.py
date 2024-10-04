import sys
input = sys.stdin.readline

N = int(input())    # 시험장 개수
lst = list(map(int, input().split()))   # 시험장의 응시자 수

B, C = map(int, input().split())    #B = 총 감독관의 감시 수, C = 부감독관의 감시 수

ans = N     # 총 감독관은 시험장의 개수만큼
for n in lst:
    if n-B > 0:     # 총 감독관이 감독한 인원 외의 인원을 부감독관이 감독함
        ans += (n-B + C-1) //C

print(ans)
