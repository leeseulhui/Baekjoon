import sys
input = sys.stdin.read

def solution(n, m):
    sorted_m = sorted(set(m))   # 중복없이 나열

    # 좌표 압축 맵 생성(인덱스 + 값을 쌍으로 묶어서 {딕셔너리} 형태로 만드는 과정)
    # enumerate 를 사용해서 키와 값을 쌍으로 만들고 딕셔너리로 반환
    compression_map = {value : idx for idx, value in enumerate(sorted_m)}

    result = [compression_map[x] for x in m]

    return result

data = input().strip().splitlines()
n = int(data[0])
m = list(map(int, data[1].split()))

result = solution(n, m)
print(*result)

