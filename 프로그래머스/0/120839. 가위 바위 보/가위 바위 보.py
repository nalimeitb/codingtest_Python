def solution(rsp):
    answer = ''
    
    for i in range(len(rsp)) :
        if rsp[i] == '2' :
            answer = answer + '0'
        elif rsp[i] == '0' :
            answer = answer + '5'
        else :
            answer = answer + '2'
    
    return answer