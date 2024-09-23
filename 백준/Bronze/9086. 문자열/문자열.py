import sys
input = sys.stdin.readline

T = int(input())    #테스트 케이스 개수 

for _ in range(T):
    S = input().strip()
    first = S[0]    #첫 글자
    last = S[-1]    #마지막 글자
    print(first + last)