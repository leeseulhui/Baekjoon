import sys
input = sys.stdin.readline

tall_box = []   # 난쟁이들 키 저장할 공간

for _ in range(9):
    tall = int(input().strip())
    tall_box.append(tall)

tot = sum(tall_box)

found = False
for i in range(9):
    for j in range(i+1, 9):
        if tot - tall_box[i] - tall_box[j] == 100:
            remain = [tall_box[k] for k in range(9) if k != j and k != i]
            found = True
            break
    if found:
        break

remain.sort()
for ans in remain:
    print(ans)



