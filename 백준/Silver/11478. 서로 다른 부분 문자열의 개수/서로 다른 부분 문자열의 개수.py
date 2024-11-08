import sys
input = sys.stdin.readline

def count_unique(s):
    unique_substrings = set()

#   부분 문자열 생성
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            unique_substrings.add(s[i:j])

    return len(unique_substrings)


s = input().strip()
print(count_unique(s))

