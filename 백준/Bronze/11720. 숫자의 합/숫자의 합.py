import sys
input = sys.stdin.readline

N = int(input()) 
numbers = input().strip()

tot = sum(int(num) for num in numbers)

print(tot)