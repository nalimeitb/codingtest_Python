def solution(my_string):
    answer = ''
    set1 = ('a', 'e', 'i', 'o', 'u')
    
    for i in range(len(my_string)) :
        if my_string[i] in set1 :
            continue
        else :
            answer = answer + my_string[i]
    
    return answer