import sys
input = sys.stdin.readline
from collections import Counter

word = input().strip()

#대소문자를 모두 대문자로 (upper 메소드 사용)
word_upper = word.upper()

#알파벳의 사용 빈도
counter = Counter(word_upper)

#그렇다면 가장 많이 사용된 알파벳은? (most_common 메소드 사용)
most_common = counter.most_common()

#가장 많이 사용된 빈도는?
max_count = most_common[0][1]

#가장 많이 사용된 알파벳이 여러개
most_used_letters = []
for letter, count in most_common:
    if count == max_count:
        most_used_letters.append(letter)

if len(most_used_letters) > 1:
    print("?")
else:
    print(most_used_letters[0])
    
   
