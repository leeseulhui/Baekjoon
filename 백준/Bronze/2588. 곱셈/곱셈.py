import sys
input = sys.stdin.readline

A = int(input())    #첫째줄 세 자리 숫자
B = int(input())    #둘째줄 세 자리 숫자

#B의 각 자리수
B1 = B % 10
B2 = (B // 10) % 10
B3 = B // 100

answer1 = A * B1
answer2 = A * B2
answer3 = A * B3
answer4 = A * B


print(answer1)
print(answer2)
print(answer3)
print(answer4) 