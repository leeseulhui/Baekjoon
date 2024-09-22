import sys
input = sys.stdin.readline

A, B = map(int, input().split())    
C = int(input())   

B = B + C   

0 <= A <= 23 and 0 <= B <= 59
0 <= C <= 1000

if B >= 60:
    A = A + B // 60 
    B = B % 60 

if A >= 24: 
    A = A % 24

print(A, B)
