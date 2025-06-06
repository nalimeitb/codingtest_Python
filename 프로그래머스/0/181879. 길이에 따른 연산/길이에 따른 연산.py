def solution(num_list):
    answer = 0
    hap = 0
    gop = 1
    
    for i in num_list :
        if len(num_list) >= 11 :
            hap = hap + i
            answer = hap
        else :
            gop = gop * i
            answer = gop
    
    return answer