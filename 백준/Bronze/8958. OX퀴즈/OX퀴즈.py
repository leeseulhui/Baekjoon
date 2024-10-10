import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    q = input().strip()

    tot_sum = 0
    current_sum = 0
    
    for answer in q:
        if answer == 'O':
            current_sum += 1
            tot_sum += current_sum
        else:
            current_sum = 0

    print(tot_sum)




