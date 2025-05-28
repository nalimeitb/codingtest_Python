def solution(q, r, code):
    answer = ''
    a = 0
    
    for i in range(len(code)) :
        a = i % q
        if a == r :
            answer = answer + code[i]
    
    return answer