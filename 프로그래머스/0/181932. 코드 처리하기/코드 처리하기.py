def solution(code):
    ret = ''
    answer = ''
    mode = 0
    
    for idx in range(len(code)) :
        if mode == 0 :
            if code[idx] != '1' :
                if idx % 2 == 0 :
                    ret = ret + code[idx]
            if code[idx] == '1' :
                mode = 1
        elif mode == 1 :
            if code[idx] != '1' :
                if idx % 2 != 0 :
                    ret = ret + code[idx]
            if code[idx] == '1' :
                mode = 0
            
    if ret == '' :
        answer = "EMPTY"
    else :
        answer = ret
        
    return answer