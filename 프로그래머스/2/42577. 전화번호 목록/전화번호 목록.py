def solution(phone_book):
    # 1. 전화번호를 sorting 
    phone_book.sort()
    # 2. sorting 한 전화번호를 2개씩 확인해서 접두어인지 본다
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True
    
print(solution(["6", "12", "6789"]))
