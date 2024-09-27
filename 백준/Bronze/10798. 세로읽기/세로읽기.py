import sys
input = sys.stdin.readline

words = []

for _ in range(5):
    words.append(input().strip())

result = ""     #결과 저장할 문자열 변수(문자열이기 때문에 배열이 아니라 "" 인 것임)

for  i in range(15):
    for word in words:
        if i < len(word):
            result = result + word[i]

print(result)