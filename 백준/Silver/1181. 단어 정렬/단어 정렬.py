import sys
input = sys.stdin.readline

n = int(input().strip())
word_box = set()

for _ in range(n):
    word = input().strip()
    word_box.add(word)

sorted_word = sorted(word_box, key= lambda x: (len(x), x))

for word in sorted_word:
    print(word)