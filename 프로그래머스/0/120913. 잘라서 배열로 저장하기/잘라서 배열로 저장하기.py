def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str), n) :
        answer.append(my_str[i:i+n])
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if len(my_str) % n == 0:
    #     for i in range((len(my_str)//n)) :
    #         answer.append(my_str[0+i*n:(i+1)*n])
    # else :
    #     for i in range((len(my_str)//n)+1) :
    #         answer.append(my_str[0+i*n:(i+1)*n])
    
    # for i in range(0, len(my_str), n) :
    #     answer.append(my_str[i:i+n])
    
    return answer