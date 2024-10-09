import sys
input = sys.stdin.readline

#심사위원의 수 
V = int(input().strip())
#심사위원이 투표한 사람
N = input().strip()

A_vote = N.count('A')
B_vote = N.count('B')


if A_vote > B_vote:
    print("A")
elif A_vote < B_vote:
    print("B")
else:
    print("Tie")
