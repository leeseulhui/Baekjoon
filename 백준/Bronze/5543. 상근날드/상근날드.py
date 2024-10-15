import sys
input = sys.stdin.readline

f_box = []

for _ in range(5):
    food = int(input().strip())
    f_box.append(food)
    
low_b = min(f_box[:3])

low_d = min(f_box[3:5])

set_menu = low_b + low_d - 50

print(set_menu)

