import sys
input = sys.stdin.readline


word = input().strip()

#크로아티아 단어를 리스트로 정의해둠
cro_word = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

#크로아티아 알파벳 개수를 세기 위한 변수
count = 0
i = 0

while i < len(word):
    #세 글자일 때
    if i < len(word) -2 and word[i:i+3] == 'dz=':
        count += 1
        i += 3
    #두 글자일 때
    elif i < len(word) -1 and word[i:i+2] in cro_word:
        count += 1
        i += 2
    else:
        count += 1
        i += 1
print(count)
