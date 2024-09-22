import sys
input = sys.stdin.readline

N = int(input().strip())    #입력 정수의 개수

numbers = list(map(int, input().split()))   #N개의 정수 리스트

v = int(input().strip())    #찾으려고 하는 정수

print(numbers.count(v))
