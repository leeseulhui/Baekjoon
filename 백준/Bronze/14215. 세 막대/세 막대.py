import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

slides = sorted([a, b, c])  #오름차순으로 정렬 -> 가장 큰 수가 자연스레 앞으로 올 것임

if slides[0] + slides[1] > slides[2]:
    print(sum(slides))

else:
    print(2 * (slides[0] + slides[1]) -1)

