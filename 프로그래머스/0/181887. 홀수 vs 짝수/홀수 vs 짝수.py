def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    
    for i in range(len(num_list)) :
        if i % 2 == 0 :
            odd = odd + num_list[i]
            
        else :
            even = even + num_list[i]
            
    if odd > even :
        answer = odd
    else :
        answer = even
            
    
    return answer