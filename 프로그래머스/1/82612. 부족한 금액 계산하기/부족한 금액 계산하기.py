import sys
input = sys.stdin.readline

def solution(price, money, count):
    ans = 0

    for i in range(1, count + 1):
        ans += price * i
        
    if ans < money:
        ans = 0
    else:
        ans = ans - money

    return ans