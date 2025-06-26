def solution(array):
    answer = 0
    tmp = ''
    
    for i in array :
        tmp = tmp + str(i)
        
    for i in range(len(tmp)) :
        if tmp[i] == '7' :
            answer = answer + 1
    
    
    return answer