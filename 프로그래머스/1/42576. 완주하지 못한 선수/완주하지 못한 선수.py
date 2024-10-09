def solution(participant, completion):
    
    # 1. 두 리스트를 sorting 
    participant.sort()
    completion.sort()
    # 2. completion list의 length 만큼 돌면서, participant에 존재하지 않는 선수 찾기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수
    return participant[len(participant) - 1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
