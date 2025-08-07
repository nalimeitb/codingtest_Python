def solution(s):
    answer = ''
    i = 0
    k = 0
    
    for j in s :
        if j != " " :
            if k % 2 == 0 :
                answer = answer + j.upper()
            else :
                answer = answer + j.lower()
            k = k + 1
        else :
            answer = answer + " "
            k = 0
        i = i + 1
        
    
    return answer