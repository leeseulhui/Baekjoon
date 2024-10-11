import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())

    tot_credits = 0
    tot_scroe = 0

    for _ in range(N):
        C, G = map(float, input().strip().split()) 
        tot_credits += int(C)
        tot_scroe += C * G

    avg = tot_scroe / tot_credits
    print(int(tot_credits), format(avg, ".1f"))
    
    