import sys
input = sys.stdin.readline

test_case = 0 

while True:
    A, B = map(int, input().split())    #두 수를 입력받아 여러 개의 테스트 케이스 처리
    if A == 0 and B == 0:
        break
    print(A + B)
    test_case += 1