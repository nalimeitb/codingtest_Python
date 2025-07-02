def solution(n):
    answer = 0
    
    list1 = list()
    i = 0
    
    while len(list1) <= 100 :
        i = i + 1
        if i % 3 != 0 and str(3) not in str(i) :
            list1.append(i)
    
    answer = list1[n-1]
    
        
    
    return answer