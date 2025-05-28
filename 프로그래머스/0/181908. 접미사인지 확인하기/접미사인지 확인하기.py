def solution(my_string, is_suffix):
    answer = 0
    my_string_list = list()
    
    for i in range(len(my_string)) :
        my_string_list.append(my_string[-i:])
    
    for k in my_string_list :
        if k == is_suffix :
            answer = 1
            break
    
    
    return answer