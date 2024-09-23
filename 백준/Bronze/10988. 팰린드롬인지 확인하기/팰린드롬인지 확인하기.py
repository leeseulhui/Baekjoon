import sys
input = sys.stdin.readline

word = input().strip()

reversed_word = word[::-1]  #[::-1] -> 단어를 거꾸로 뒤집어주는 슬라이싱 기법

if word == reversed_word:
    print(1)
else:
    print(0)
