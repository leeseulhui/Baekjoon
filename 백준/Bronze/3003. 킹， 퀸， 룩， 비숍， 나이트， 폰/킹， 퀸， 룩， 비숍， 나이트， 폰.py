import sys
input = sys.stdin.readline

#구성된 피스들
required = [1, 1, 2, 2, 2, 8]

#찾은 흰색 피스들 = 리스트로 묶어줄거임
white = list(map(int, input().split()))

#결과 저장
result = []

for correct, user in zip(required, white):
    result.append(correct - user)

print(' '.join(map(str, result)))