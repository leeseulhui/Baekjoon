import sys
input = sys.stdin.readline

hat_box = []
for _ in range(9):
    hat = int(input().strip())
    hat_box.append(hat)

tot = sum(hat_box)

#두 명의 난쟁이 찾기
found = False
for i in range(9):
    for j in range(i+1, 9):
        if tot - hat_box[i] - hat_box[j] == 100:
            p1, p2 = hat_box[i], hat_box[j]

            hat_box.remove(p1)
            hat_box.remove(p2)

            found = True
            break
    if found:
        break

for hats in hat_box:
    print(hats)


