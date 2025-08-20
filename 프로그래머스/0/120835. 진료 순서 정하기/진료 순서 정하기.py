def solution(emergency):
    answer = []
    list1 = emergency[:]
    
    list1 = sorted(list1, reverse = True)
    
    for i in emergency :
        answer.append(list1.index(i)+1)
        
        
    
    return answer