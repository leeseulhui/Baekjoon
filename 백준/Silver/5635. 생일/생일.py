import sys
input = sys.stdin.readline
from datetime import datetime

n = int(input().strip())

min_age_name = ""
max_age_name = ""
min_date = datetime(2011,1,1)
max_date = datetime(1990,1,1)


for _ in range(n):
    date = input().strip().split()
    name = date[0]

    d, m, y = map(int, date[1:])
    birth = datetime(y, m, d)

    if birth < min_date:
        min_date = birth
        min_age_name = name

    if birth > max_date:
        max_date = birth
        max_age_name = name

print(max_age_name)
print(min_age_name)

