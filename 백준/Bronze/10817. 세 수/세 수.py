import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

numbers = [A, B, C]

numbers.sort()  # sort -> 오름차순으로 정렬 

print(numbers[1])