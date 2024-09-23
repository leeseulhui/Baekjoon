import sys
input = sys.stdin.readline

S = input().strip()

#리스트 초기화
words = [-1] * 26

#리스트 순회
for index in range(len(S)):
    char = S[index]
    char_index = ord(char) - ord('a') 
    if words[char_index] == -1: 
        words[char_index] = index

print(' '.join(map(str, words)))