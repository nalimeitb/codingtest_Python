def solution(array, n):
    answer = 0
    min1 = None
    
    for i in array :
        if min1 == None :
            min1 = (i, abs(n-i))
            
        elif min1[1] > abs(n-i) :
            min1 = (i, abs(n-i))
        
        elif min1[1] == abs(n-i) :
            if min1[0] > i :
                min1 = (i, abs(n-i))
            else :
                continue
            
        else :
            continue
        
    
    answer = min1[0]
    
    return answer