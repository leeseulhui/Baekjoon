import sys
import math
input = sys.stdin.readline

M = int(input().strip())
N = int(input().strip())

num_space = []    # 완전제곱 저장할 공간

for k in range(1, int(math.sqrt(N) + 1)):
    num = k * k
    if M <= num <= N:
        num_space.append(num)

if num_space:
    sum_num = sum(num_space)
    min_num = min(num_space)

    print(sum_num)
    print(min_num)
else:
    print(-1)
