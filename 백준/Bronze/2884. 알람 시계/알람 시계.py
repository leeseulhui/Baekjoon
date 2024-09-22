import sys
input = sys.stdin.readline

H, M = map(int, input().split())

0 <= H <= 23 and 0 <= M <= 59

if M >= 45:
    M -= 45
else:
    M = M + 60-45
    H -= 1
    if H < 0:   #만약 시간이 0시였다면 23시로 바꿔줘야겠지
        H = 23

print(H,M)