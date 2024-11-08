import sys
input = sys.stdin.readline

def solution(arr):
    min_value = min(arr)    # 가장 작은 수 찾음
    arr.remove(min_value)

    if not arr:
        return [-1] # 배열이 비었을 경우 -1 리턴
    
    return arr