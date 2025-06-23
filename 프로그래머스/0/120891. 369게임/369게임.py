def solution(order):
    answer = 0
    order = str(order)
    set1 = ('3', '6', '9')
    
    for i in order :
        if i in set1 :
            answer = answer + 1
        
    
    return answer