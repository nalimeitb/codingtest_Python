def solution(my_string, n):
    answer = ''
    lenstr = len(my_string)
    
    answer = my_string[lenstr-n:]
    
    return answer