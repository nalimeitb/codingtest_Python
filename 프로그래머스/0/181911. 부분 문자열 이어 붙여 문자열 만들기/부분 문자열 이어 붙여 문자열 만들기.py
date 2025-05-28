def solution(my_strings, parts):
    answer = ''
    i = 0
    
    for s,e in parts :
        answer = answer + my_strings[i][s:e+1]
        i = i + 1
                                        
    return answer