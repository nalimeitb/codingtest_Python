def solution(num_list):
    answer = 0
    k = 0
    
    for i in num_list :
        while i != 1 :
            k = k + 1
            if i % 2 == 0 :
                i = i / 2
            else :
                i = (i-1) / 2
    
    answer = k
    
    return answer