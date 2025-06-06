def solution(my_string, alp):
    answer = ''
    list1 = list(my_string)
    
    for i in range(len(list1)) :
        if list1[i] == alp :
            list1[i] = list1[i].upper()
            answer = answer + list1[i]
        
        else :
            answer = answer + list1[i]
    
    return answer