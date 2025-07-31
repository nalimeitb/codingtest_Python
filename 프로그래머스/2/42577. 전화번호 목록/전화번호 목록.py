def solution(phone_book):
    answer = True
    
    phone_book = set(phone_book)
    
    for i in phone_book :
        for k in range(len(i)) :
            if i[:k] in phone_book :
                return False
    
    return answer