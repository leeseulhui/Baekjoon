import sys
input = sys.stdin.readline

A, I = map(int, input().split())

# 저작권 있는 멜로디
melody = A * (I - 1) + 1

print(melody)