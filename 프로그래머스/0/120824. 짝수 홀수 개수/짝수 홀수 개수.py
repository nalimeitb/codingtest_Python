def solution(num_list):
    answer = []
    hol = 0
    jjak = 0
    
    for i in num_list :
        if i % 2 == 0 :
            jjak = jjak + 1
        else :
            hol = hol + 1
            
    answer.append(jjak)
    answer.append(hol)
    
    
    return answer