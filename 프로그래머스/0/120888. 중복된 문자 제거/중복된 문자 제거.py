def solution(my_string):
    answer = ''
    
    for i in range(len(my_string)) :
        if my_string[i] not in answer :
            answer = answer + my_string[i]
    
    return answer