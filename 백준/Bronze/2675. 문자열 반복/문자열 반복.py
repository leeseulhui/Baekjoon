import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = input().split()   #한 줄에서 나타내야 하니까 같이 써야함.
    R = int(R)  
    
    P = ""  #결과 문자열 초기화함

    for char in S:
        P = P + char * R

    print(P)
    
    
