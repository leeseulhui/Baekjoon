import sys
from datetime import datetime, timedelta
input = sys.stdin.readline


now_time = input().strip()
start_time = input().strip()

now = datetime.strptime(now_time, "%H:%M:%S")
start = datetime.strptime(start_time, "%H:%M:%S")

if start > now:
    remain_time = start - now
else:
    remain_time = (timedelta(days=1) - (now - start))

print((datetime.min + remain_time).strftime("%H:%M:%S"))